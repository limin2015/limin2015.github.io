---
layout:     post
title:      paper-SM-Centric Scheduing on GPU
keywords:   paper-VersaPipe-2017
category:   [paper]
tags:       [paper]
---



本文是对于以下2篇文章的总结：（第一篇文章的写作太好了，学习！！）

 - **SM-Centric Transformation, Circumventing Hardware Restrictions for Flexible GPU Scheduling**

- **Enabling and Exploiting Flexible Task Assignment on GPU through SM-Centric Program Transformations**



# 1. 出处：

BoWu 的 PACT’14的短文，和ICS’15的长文



# 2. persistent thread存在的问题

- The first limitation comes from the randomness in the hard- ware scheduler. Our experiments showed that the schedul- ing is not round-robin, contrary to common perception, and does not guarantee an even distribution of thread blocks, even if the number of thread blocks is small. Hence, persistent threads may underutilize hardware resource if some SMs obtain less thread blocks than others.

- persistent threads has no support for deciding on which SM a task should run, which is important for some optimizations of locality enhancement.


# 3. main methods:

本文解决了persistent thread存在的2个问题，提供了a method to map
tasks to SMs and enable parallelismcontrol on GPU. 
主要用到的方法是：**SM-centric task selection** and a **filling-retreating scheme**.


## 3.1 SM-Centric Task Selection

原有的方法是怎样的：

The GPU threads are grouped into thread blocks (the workers),（note：这里的worker代表软件层面的block，job代表要程序要处理的task） each processing a job. Usually, the programmer builds the mapping between jobs and workers, as shown in Figure 1 (a). Since the workers are arbitrarily scheduled to SMs, the mapping between jobs and SMs is also arbitrary（这种方式是最普通的方式）. Persistent threads, as illustrated in Figure 1 (b), maintains a global job queue. The workers grab jobs from the queue once they are idle. As such, persistent threads can map jobs to workers(这种方式类似于我在神威上的：fetch_add方式的动态任务调度). However, the thread block’s placement on SM is controlled by hardware, so is the binding between tasks and SMs. 

本文的方法：

The SM-centric task selection  **breaks the binding between workers and jobs, but maps jobs to SMs instead**. 
（这种方式：类似我的想法：SM内部可以做好几个任务。它抽象了一下！！）
As shown in Figure 1 (c), before the kernel launches, a job queue is created for each SM. 
When a worker begins execution, it first checks the SM it runs on and processes the next job in the job queue associated with the host SM.  Note that different from persistent threads, a worker only processes one job. 

Therefore, for this idea to work, the number of workers scheduled by an SM should be at least the same as the number of jobs in the associated job queue. This property, however, does not hold due to the randomness in the hard- ware scheduler, and create a program correctness problem。（为什么呢: 因为block被调度到SM上是随机的。比如共有2个SM，开了4个块，不能保证，硬件调度的时候，每个SM上被分到2个块。因为这是随机的，跟硬件相关的。）

那么，如何解决这个问题呢？设置一个count，在每个SM上数一下，目前在这个SM上运行的block的个数，若超过了2，则啥也不做。这样就能保证每个SM上被分配到2个block。（下面的filling-retreating scheme即使这种方法！！）

有一个问题就是：若某个SM上分到的block超过了threshold，当前块就exit，那么按道理来说，每个SM上分到的逻辑block的数目不是一样的，但是每个SM处理的任务是均衡的。
那么少分到的那个SM，如果分到的逻辑block太少，没法掩盖访存延迟咋办？

是这样的：他先看看一个SM上最大可以分配到的活的block数-M，在每个SM上的设置的job数，即实际使用的block数（与job数一样），记做n， 
n小于M， 所以，硬件调度的时候，每个SM上可以分到小于M个block，大于n个block（大于n可以保证吗，貌似不可以！！！）（因为只要硬件闲着，新的block就可以分配到此SM），这样的话，我们在每个SM上只使用前n个block，就能保证，每个SM上有固定的n个block在run。

每个SM上可以分到大于n个block，是如何保证的呢？？
paper中有一句话：（应该是设置n比较小）

The basic idea is to maintain a fixed number (usually small) of workers on each SM, which process all jobs in the corresponding queue. 




## 3.2 filling-retreating scheme

The basic idea is to maintain a fixed number (usually small) of workers on each SM, which process all jobs in the corresponding queue. By analyzing and characterizing the GPU kernel at runtime, we determine **the maximum number of active thread blocks on each SM, denoted as M**. 

Given N SMs, we generate M×N workers. We found that the hardware scheduler always distributes all workers to SMs, as long as the hardware resources are enough to accommodate that many. This process is called **filling**. 

Afterwards, to control the number of active workers per SM (i.e., wantedNumPerSM, and wantedNumPerSM <M),
the extra workers (M −wantedNumPerSM) exit immediately. 
This process is called **retreating**. 
Based on these two processes, we can control which jobs should be processed by which SM and how many workers per SM.