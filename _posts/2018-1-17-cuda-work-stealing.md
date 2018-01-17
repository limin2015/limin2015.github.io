---
layout:     post
title:      cuda-work-sharing-and-work-stealing
keywords:   work-stealing
category:   CUDA
tags:		[CUDA编程]
---

任务调度里面的work stealing and work sharing.


# work stealing


1. work stealing试用的场景

对于一个线程池，**每个线程有一个队列**，想象这种场景，有的线程队列中有大量的比较耗时的任务堆积，而有的线程队列却是空的，现象就是有的线程处于饥饿状态，而有的线程处于消化不良的状态，这时就需要一种方法来解决这个问题。
需要work steal，顾名思义就是任务窃取，当一个线程处于饥饿状态时，它就会去其它的线程队列中窃取任务，解决线程饥饿导致的效率底的问题。




2. work stealing的实现要点

每个工作线程将任务放到它内部的队列中；
- 队列是一个双端队列，支持LIFO的push_front和pop_front操作和FIFO的take操作。
- 工作线程处理任务通过LIFO来处理最新的任务。
- 当一个线程处理完了队列中的任务之后，它会试图窃取其他线程队列的任务，根据FIFO从队列的尾部取任务。
- 如果窃取任务失败则继续尝试，直到所有的线程队列都没有任务了。

如图所示：

![](/images/cuda/work-stealing-1.png)


3. worksteal值得探讨的问题 

（1）worksteal的适用场景

当任务之间的耗时相差比较大。，即有的任务很耗时，有的任务很快完成，这种用worksteal很合适。若很平均，则不用使用，因为work-stealing本身有很多开销。

（2）窃取任务的策略

有很多strategy， 比如从任务最多的线程中窃取（贪心）或随机窃取。

（3）窃取任务的粒度 

是每次窃取一个任务还是窃取一批任务也是需要考量的，如果窃取的一批任务比较耗时，又会导致其它线程来窃取，这样造成了无谓的消耗；如果一次窃取一个任务，而任务很快完成，这又导致重新窃取，降低了效率。这个粒度也是需要根据实际情况调整的。


4. 其他资料

[worksteal thread pool源码](https://github.com/qicosmos/cosmos/tree/master/worksteal)

https://blogs.msdn.microsoft.com/jennifer/2009/06/26/work-stealing-in-net-4-0/

5. 引用

基本上出自下面的blog：

[stackoverflow-work stealing algorithm](https://stackoverflow.com/questions/9081382/work-stealing-algorithm)

[Work-Stealing in .NET 4.0](https://www.cnblogs.com/qicosmos/archive/2015/11/18/4975454.html)

[Scheduling Multithreaded Computations by Work Stealing](http://supertech.csail.mit.edu/papers/steal.pdf)



# work sharing

1. 