---
layout:     post
title:      paper-Automatically Scheduling Halide Image Processing Pipelines
keywords:   paper-halide2016
category:   [paper]
tags:       [paper]
---

# 出处：
2016年，《Acm Transactions on Graphics》（ccf-a）


# 要解决的问题：

1.halide语言成为一个有效的产生高性能的图像处理代码的系统。他的工作方式是这样的：程序员提供如何并行的策略，即schedule，然后halide将schedule自动的实现到具体的硬件平台上。这种方法存在一个问题：程序员需要对hpc非常了解，而且schedule的生成其实是最critical的步骤。


# 摘要：

为了解决上面提到的问题，使得普通程序员也能够利用halide生成高效的代码，本文提出了一个自动产生高性能的schedule的算法。


# 前人工作

TODO


# 主要内容：

## halide简介

**主要思想**：将schedule和自动生成硬件相关的代码进行分离。（这个思想也被tvm使用。）

**Halide’s scheduling primitives**：

 **compute_at**：在下面tvm中介绍。

**reorder**：调整循环顺序。

 **tile**：分块。


下面的是tvm提供的schedule：（仔细理解一下！！）

A Schedule is a set of transformation of computation that transforms the loop of computations in the program.
A schedule can be created from a list of ops, by default the schedule computes tensor in a serial manner in a row-major order.

[tvm提供的schedule](http://docs.tvmlang.org/tutorials/language/schedule_primitives.html#sphx-glr-tutorials-language-schedule-primitives-py)

默认schedule：串行执行。

bind： bind  can bind a specified axis with a thread axis, often used in gpu programming.

compute_at： 对于一个含有多个operator（多个计算函数）的schedule来说，一般默认情况下，tvm会挨个计算每一个函数的结果，即先计算中中间的一些结果之后，在计算下一个operator的结果。 使用compute_at可以使得某个operator和另一个operator融合在一起计算，提高Producer-Consumer Locality。

eg：（1）default：

    A = tvm.placeholder((m,), name='A')
    B = tvm.compute((m,), lambda i: A[i]+1, name='B')
    C = tvm.compute((m,), lambda i: B[i]*2, name='C')

    s = tvm.create_schedule(C.op)
    print(tvm.lower(s, [A, B, C], simple_mode=True))


    output：
    produce B {
    for (i, 0, m) {
        B[i] = (A[i] + 1.000000f)
        }
    }
    produce C {
    for (i, 0, m) {
        C[i] = (B[i]*2.000000f)
        }
    }

    （2）使用compute_at：
    A = tvm.placeholder((m,), name='A')
    B = tvm.compute((m,), lambda i: A[i]+1, name='B')
    C = tvm.compute((m,), lambda i: B[i]*2, name='C')

    s = tvm.create_schedule(C.op)   
    s[B].compute_at(s[C], C.op.axis[0])
    print(tvm.lower(s, [A, B, C], simple_mode=True))

    output：
    produce C {
    for (i, 0, m) {
        produce B {
        B[i] = (A[i] + 1.000000f)
        }
        C[i] = (B[i]*2.000000f)
    }
    }





compute_inline:将某一个stage（某一个中间的operator）内联，直接替换成表达式（有点类似于函数内联）。

compute_root：move computation of one stage to the root。有点类似于compute_at的逆运算。

fuse：合并两个for循环为一次for循环。

split：  split a specified axis into two axises by factor（or  nparts）。（其实就是一维数组的任务分配，分块）






## 正式介绍算法前的例子：（通过特定的程序，看看如何生成schedule）

//补：把paper中的截图，粘过来。


1. Scheduling for Producer-Consumer Locality

**疑问**：
（1）Producer-Consumer Locality是什么？

为了计算out，一般都会需要计算一些中间结果（比如一个数组，mid-buffer）；
如果先把mid-buffer全部计算出来，再计算out，那么Producer-Consumer Locality就会比较低，大部分情况下，会导致memory-bound。


策略：

(1)一种是：为了提高并行度，先计算中间结果数组，再计算最终的结果out数组。

（2）一种是：最大化p-c-locality，以计算out为准，没产生一个out的元素之前，把它需要的中间结果的值计算出来。但是这样通过会带来冗余计算。

（3）一种是：前两者的折中。在最内层分块（这种策略叫overlapped tiling），计算一块的中间数组，然后接着计算此块的out。




2. Scheduling for Input Reuse

**疑问**：
（1）Input Reuse 是什么？

这个考虑的其实是一个函数中，对于输入数据的重用（我平常接触的都是这种），比如GEMM。input的reuse对于稠密线性代数函数和卷积的计算特别关键。（其实就是对于计算占有的函数的优化很关键）。



3. Function Bounds Analysis

（1）Function Bounds是什么：

the compiler must be able to determine the appropriate loop bounds and intermediate buffer sizes

**举例**来说，
编译器根据输入的expression来分析函数的bound，比如：
当out 数组的界属于：(xmin..xmax,ymin..ymax) 时（逗号前时x的范围，逗号后时y的范围），输入数组和中间数组的界是：
blurx: (xmin..xmax, ymin-1..ymax+1) in:
(xmin-1..xmax+1, ymin-1..ymax+1)


（2）那么如何确定函数的bound呢：

Starting from the output function, bounds inference propagates up the function dependency chain, ascribing bounds to all functions in the program DAG.

TODO: 底下这段没有看明白！！

When the Halide compiler cannot infer tight bounds for a function (e.g., due to data-dependent access by a con- sumer), the programmer can explicitly provide bounds to assist the compiler in generating efficient code (e.g., the programmer may have static knowledge that all accesses to a lookup table will be in the range 0..8)



## 本文的算法

main idea：partition the functions in a large Halide program into groups (subprograms), and independently perform producer-consumer locality and input reuse locality transformations on these groups.

对于一个group的schedule的计算顺序，本文只considers a narrower space schedules that tile the loop nest corresponding to the group’s output function. 
The computation of all other functions in the group is placed within this tiled loop (a single placement decision is made for all producers)。

意思就是：只对group的输出的loop循环进行tiling，这个组里面的其他函数被放在这个output的loop中。//这个地方是一个局限（有没有在这种策略下，不能取得好性能的例子？？？）
这种调度策略，有一定的缺陷，不适用于这种情况：
input programs are constrained to use only one update rule per function。（这个不大理解：输入程序中，一个函数使用一种更新策略。）

schedule算法的输入是：输入program（包含多个function），输出的参数个数（an estimate of concrete bounds for the domain of the program’s output function），concrete bounds for any inputs that cannot be directly inferred from the output bounds。




### 1. Function Preprocessing

（1）估计计算开销：

对于每一个function，估计计算一个value的开销（算数运算的个数）。比如加，减，乘这种，算一个运算，除法和超越函数，算好几个运算。（这个和hpc中的gflops有点像）

（2）计算concrete bounds：

use Halide’s bounds analysis to compute concrete bounds for all functions.（具体怎么做的，需要看halide系统了的，或者之前的paper）

（3）计算per-direction input reuse：

为了确定用哪种调度，我们需要知道，for each function, which **domain-iteration order**（这个是啥意思？？） yields the highest amount of input data reuse.

即计算结果的时候，若循环，是采取行优先的循环，还是列优先的循环，分别评估一下它的数据重用。（这里的行优先是什么意思啊？？？）

评估的时候，要评估输出函数的所有前继函数的数据重用的和。


### 2. Function Grouping and Tiling：（重点）

分组的作用：

Grouping seeks to identify points in the program where it is beneficial to restructure computation ordering 
to improve producer-consumer locality. This requires determining if and how to tile consumer loop nests and where to place the computation of producer functions within these loop nests.（这句话说得太清楚了，赞！！）

如何分组：

1.每个组里的functions，只有一个是输出function，相当于这个group的数据流图只有一个聚点。
2.使用贪心，迭代的方法把functions分到不同的group中：

- （1）初始化：每个function是一个group，这些组被分别tiled，然后计算每个组的input data reuse。
- （2）迭代：each iteration attempts to **increase producer-consumer locality** by merging two existing groups.
- （3）迭代终止条件：当合并剩下的groups没有带来性能提升时。（when the auto- scheduler estimates there is no performance benefit to merging any of the remaining groups）

每次迭代：
- （a）Enumerate all remaining group merging opportunities
- （b）For each merging opportunity, estimate the performance benefit of merging the two groups. The act of evaluating the benefit of a merge requires determining a tiled loop-nest structure for the potential merged group.
- （c）Select the merge that yields the greatest performance benefit (provided at least one merge that provides benefit does exist) and merge the two groups.

Initialization: Tiling for Input Data Reuse：

引入了Pure functions的概念：functions that do not contain Halide update definitions or reduction domains, such as small stencils—exhibit high input locality without tiling.(不包含halide更新定义和规约域的函数，比如一个小的stencil计算，即使不tiing也会有很好的input locality。)
所以，下面的tiling，只针对non-pure  functions：

采用了一个单层的memory hierarchy模型。需要有策略决定，tile-size是多大（minimizes the number of loads required to compute the final output）？
算法如下：listing-1：TODO(截图)


评价：这个tiling函数是简化了的，对于gpu这种具有多层memory hierarchy的硬件来说，需要考虑的更多一些。（gpu还需要考虑global-mem的合并访问，防止thread divengence，利用好share-mem）



Enumerating Merging Opportunities：（列举出所有可能的合并机会）

two groups g1 and g2 are candidates for merging if the output of group g1 is consumed by a function in g2.（两个组能合并的条件是：一个组的输出被另一个组的某一个函数所使用），更明确一点：the output of g1 is consumed by functions in exactly one group，不能被好几个组都使用。



Evaluating Potential Merges：

若合并两个组，如何评估它的收益呢？如何知道合并是有益的呢？如果由于合并带来的producer-consumer locality收益大于冗余计算带来的开销，那这种合并就是值得的。
当然，具体的，需要重新设置tiling的大小，来看看收益和开销到底是多大？

算法如下：listing-2：TODO(截图)







### 3. Function Inlining：

这一步实在预处理之后，group之前做的。

函数inline：跟分组差不多，区别在于：group是procuder function放到consumer function的loop中执行，挪了一下位置。
而inline是把procuder function展开之后放到consumer function的loop中执行，相当于没有使用数组等数据结构来存储中间结果，使用寄存器来通信的，访存效率更高。

如何做的：采取跟分组类似的做法，但有3点不同：
- （1）inlining can be applied to functions with multiple consumers。为了简单起见，本文只考虑一个函数的被inline的情况。
Either a function is inlined into all of its consumers (essentially removing the function from the program DAG), 
or to none of its consumers (it remains in the DAG and is subsequently considered for grouping as described in Section 4.2)

- （2）When evaluating the performance benefit of inlining, the auto- scheduler must consider the cost of inlining a function into all consumers (not just a single consumer as was the case during group merging decisions).（当评估inline带来的收益时，要考虑把一个函数inline进所有的consumer functions中的开销）

- （3）The auto-scheduler does not use bounds analysis to estimate the arithmetic cost of the results of an inlining transformation. Instead it substitutes the producer function expression into the consumer function and reevaluates the arithmetic cost of the new expression. This is a more accurate measure of cost because bounds analysis can overestimate the actual number of values required by a consumer（在评估inline transformation的计算代价时，不使用bound analysis，而是直接计算inline后产生的新表达式的算数开销。）//这点有点不明白，原来是用bound评估开销的吗？？


### 4. Final Schedule Generation：

inline和合并group之后的结果是：a list of groups, each with a specified loop tiling。

接下来，需要：perform final optimizations and to generate a complete Halide schedule for each of these groups：

- （1）首先，对于每一个组的输出函数的loops：进行reorder（按照输入locality最大的原则）。注意：为了保证空间局部性和向量化的需要，输出函数的最内层的loop不能移动（这个地方没有想明白）。
- （2）如果最内层的循环次数比较小，则展开最内存循环，并vectorize。

- （3）并行化最外层的loop：parallelizes as many outermost dimensions of the loop nest as necessary to obtain sufficient multi-core parallelism for the target machine


# 实验结果：

准备了14个benchmark，包含gemm，卷积，VGG网络等。

## Server CPU Performance


## Specializing Schedules to Problem Size


## Comparison with Manual Scheduling Effort


## Portability to Different Architectures

gpu-k40：

designating the outer tile loops as GPU block grid dimensions and the inner tile loops as GPU thread block dimensions. All intermediate buffers within a group are allocated in GPU shared memory。（外层循环代表第几块，内层循环代表每一块中的线程。然后中间buffer存到share-mem中）。

但是gemm的性能比较差：这是由于本文的auto-scheduler只考虑了一级缓存，而gemm要充分利用各级的缓冲，才能最终计算的好。
auto-scheduler在其他的函数中，性能还不错，是由于，内核融合带来了巨大的节省。

我感觉：对于多个memory-bound的函数，这种auto-scheduler可以带来的性能提升比较大。而对于gemm这种极度计算占有的函数，不大好了的。





# 总结，未来的改进点：

1. Extending our approach to hierarchical levels of tiling：OK！！

2. reasoning about the effects of data layout on vector code generation：这个如何理解？？？

3. We are interested in exploring interfaces for the auto-scheduler to accept partially written schedules by experts, and then fill in the missing details。


