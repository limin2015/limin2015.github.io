---
layout: post
title:  CUDA性能优化-调优工具
keywords: CUDA
categories : [CUDA]
tags : [CUDA编程]
---

调优工具的使用。。。。。。


# 调优工具相关：



## nvidia 官方文档：

[链接](http://docs.nvidia.com/cuda/profiler-users-guide/index.html#axzz30ouNvjWo)


## device上可以printf吗？

Specifically, for devices with compute capability less than 2.0, the function cuPrintf is called;     otherwise, printf can be used directly.

高于2.0的机器，编译的时候加上： -arch=sm_20， 直接调用printf（用法同普通的c程序）就可以实现。


## gprof:

http://blog.csdn.net/stanjiang2010/article/details/5655143

疑问：这是cpu程序的工具。不可以采集cuda程序的性能参数吗。


##  nvprof 和 nvvp（可产生sass代码）

**nvprof**：

1. 不加任何参数时：

	nvprof ./a.out
		
显示结果：
profiling result中显示的是kernel执行的time情况
api calls则显示的是程序调用的api所耗费的time情况


		==8641== Profiling application: ./test
		==8641== Profiling result:
		Time(%)      Time     Calls       Avg       Min       Max  Name
		99.55%  1.3032ms       602  2.1640us  2.1440us  3.5200us  void gemvKernel<int=16, int=32>(float*, float*, float*, float*, int, int)
		0.32%  4.1600us         4  1.0400us     704ns  1.3760us  [CUDA memcpy HtoD]
		0.14%  1.7920us         2     896ns     896ns     896ns  [CUDA memcpy DtoH]

		==8641== API calls:
		Time(%)      Time     Calls       Avg       Min       Max  Name
		62.07%  341.21ms         6  56.868ms  7.7290us  340.81ms  cudaMalloc
		36.26%  199.33ms         1  199.33ms  199.33ms  199.33ms  cudaDeviceReset
		1.26%  6.9176ms       602  11.491us  10.591us  44.810us  cudaLaunch
		0.16%  872.59us      3612     241ns     212ns  7.1790us  cudaSetupArgument
		0.06%  319.49us         6  53.248us  8.2680us  147.39us  cudaFree
		0.05%  275.97us        91  3.0320us     150ns  126.52us  cuDeviceGetAttribute
		0.05%  266.56us       602     442ns     415ns  2.2540us  cudaConfigureCall
		0.05%  248.20us         1  248.20us  248.20us  248.20us  cudaGetDeviceProperties
		0.02%  126.21us         1  126.21us  126.21us  126.21us  cuDeviceTotalMem
		0.02%  113.65us         6  18.941us  10.221us  36.825us  cudaMemcpy
		0.01%  31.357us         1  31.357us  31.357us  31.357us  cuDeviceGetName
		0.00%  12.188us         2  6.0940us  5.1780us  7.0100us  cudaEventRecord
		0.00%  9.2380us         1  9.2380us  9.2380us  9.2380us  cudaGetDevice
		0.00%  8.3050us         1  8.3050us  8.3050us  8.3050us  cudaDeviceSynchronize
		0.00%  4.7870us         2  2.3930us  1.1650us  3.6220us  cudaEventCreate
		0.00%  4.6530us         1  4.6530us  4.6530us  4.6530us  cudaEventSynchronize
		0.00%  2.7570us         1  2.7570us  2.7570us  2.7570us  cudaEventElapsedTime
		0.00%  1.8990us         3     633ns     142ns  1.4310us  cuDeviceGetCount
		0.00%     920ns         3     306ns     157ns     527ns  cuDeviceGet


2. 
achieved_occupancy参数：每个sm在每个cycle能够达到的最大activewarp 占总warp的比例。

		nvprof --metrics achieved_occupancy ./a.out


3. gld_throughput: global load throughput (查看memory 的throughput)

		nvprof --metrics gld_throughput ./a.out

 

4. gld_efficiency: global memory loadefficiency: device memory bandwidth的使用率

		nvprof –metrics gld_efficiency ./a.out


5. 查看运行时候的信息：IPC（instruction per cycle） 

		nvprof --metrics ipc ./a.out

6. 查看所有的以上信息：


		nvprof --metrics all ./a.out

	结果如下：

		Metric Name         Metric Description    Min   Max    Avg
	    inst_per_warp     Instructions per warp  181.000000  181.000000  181.000000
	    branch_efficiency Branch Efficiency     100.00%   100.00%   100.00%
		warp_execution_efficiency  Warp Execution Efficiency 54.94% 54.94% 54.94%
	    warp_nonpred_execution_efficiency Warp Non-Predicated Execution Efficiency 53.04% 53.04% 53.04%
		inst_replay_overhead   Instruction Replay Overhead 0.011050 0.021754 0.011068
		shared_load_transactions_per_request Shared Memory Load Transactions Per Request  1. 1. 1.
		shared_store_transactions_per_requestShared Memory Store Transactions Per Request 1.  1. 1.
		local_load_transactions_per_request  Local Memory Load Transactions Per Request 0. 0.  0.
		local_store_transactions_per_request  Local Memory Store Transactions Per Request 0. 0. 0.
		gld_transactions_per_request  Global Load Transactions Per Request  8.  8.  8.
		gst_transactions_per_request   Global Store Transactions Per Request 1. 1.  1.
		shared_store_transactions   Shared Store Transactions  272   272  272
		shared_load_transactions   Shared Load Transactions    288   288   288
		local_load_transactions   Local Load Transactions      0    0  0
		local_store_transactions  Local Store Transactions      0    0    0
		gld_transactions   Global Load Transactions    1024  1024 1024
		gst_transactions  Global Store Transactions    16    16     16
		sysmem_read_transactions   System Memory Read Transactions  0   0    0
		sysmem_write_transactions System Memory Write Transactions 5   5     5
		 l2_read_transactions    L2 Read Transactions  400   488  426
	     l2_write_transactions  L2 Write Transactions    29  29    29
		global_hit_rate   Global Hit Rate  62.50%  62.50%   62.50%
		local_hit_rate   Local Hit Rate       0.00%       0.00%       0.00%
		gld_requested_throughput Requested Global Load Throughput 3.6516GB/s 4.3646GB/s 3.9730GB/s
		gst_requested_throughput  Requested Global Store Throughput  38.950MB/s  46.556MB/s  41.008MB/s
		gld_throughput  Global Load Throughput  3.6516GB/s  4.3646GB/s  3.9730GB/s
		gst_throughput Global Store Throughput  155.80MB/s  186.22MB/s  168.80MB/s
		local_memory_overhead  Local Memory Overhead   0.00%   0.00%   0.00%
		tex_cache_hit_rate    Unified Cache Hit Rate    62.12%   62.12%   62.12%
		l2_tex_read_hit_rate  L2 Hit Rate (Texture Reads)   100.00%   100.00%   100.00%
		l2_tex_write_hit_rate L2 Hit Rate (Texture Writes) 100.00%   100.00%   100.00%
		tex_cache_throughput   Unified Cache Throughput  4.8688GB/s  5.8195GB/s  5.2974GB/s
		l2_tex_read_throughput L2 Throughput (Texture Reads)  3.6516GB/s  4.3646GB/s  3.9730GB/s
		l2_tex_write_throughput  L2 Throughput (Texture Writes)  155.80MB/s  186.22MB/s  168.80MB/s
		l2_read_throughput     L2 Throughput (Reads)  3.8037GB/s  5.4085GB/s  4.4154GB/s
		l2_write_throughput   L2 Throughput (Writes)  282.39MB/s  337.53MB/s  306.13MB/s
	    sysmem_read_throughput  System Memory Read Throughput  0.00000B/s  0.00000B/s  0.00000B/s
		sysmem_write_throughput  System Memory Write Throughput  48.688MB/s  58.195MB/s  51.498MB/s
		local_load_throughput    Local Memory Load Throughput  0.00000B/s  0.00000B/s  0.00000B/s
		local_store_throughput   Local Memory Store Throughput  0.00000B/s  0.00000B/s  0.00000B/s
		shared_load_throughput  Shared Memory Load Throughput  10.955GB/s  13.094GB/s  11.920GB/s
		shared_store_throughput Shared Memory Store Throughput  10.346GB/s  12.366GB/s  11.258GB/s
		gld_efficiency  Global Memory Load Efficiency     100.00%     100.00%     100.00%
		gst_efficiency  Global Memory Store Efficiency      25.00%      25.00%      25.00%
		tex_cache_transactions  Unified Cache Transactions 512      512     512
		flop_count_dp     Floating Point Operations(Double Precision)   0     0       0
		flop_count_dp_add    Floating Point Operations(Double Precision Add)  0    0   0
		flop_count_dp_fma   Floating Point Operations(Double Precision FMA)  0    0   0
		flop_count_dp_mul   Floating Point Operations(Double Precision Mul)   0   0  0
		flop_count_sp     Floating Point Operations(Single Precision)  4576  4576  4576
		flop_count_sp_add   Floating Point Operations(Single Precision Add)  480   480  480
	    flop_count_sp_fma   Floating Point Operations(Single Precision FMA) 2048  2048  2048
		flop_count_sp_mul    Floating Point Operation(Single Precision Mul)  0    0   0
		flop_count_sp_special  Floating Point Operations(Single Precision Special)  0  0   0
		inst_executed  Instructions Executed    2896        2896        2896
		inst_issued  Instructions Issued   2928        2928        2928
		sysmem_utilization  System Memory Utilization Low (1)  Low (1)  Low (1)
		stall_inst_fetch    Issue Stall Reasons (Instructions Fetch)  7.71%  14.94% 10.39%
		stall_exec_dependency Issue Stall Reasons (Execution Dependency) 33.04%  36.40% 34.86%
		stall_memory_dependency Issue Stall Reasons (Data Request)  30.25%  33.20%  31.87%
		stall_texture Issue Stall Reasons (Texture)   0.00%   0.00%   0.00%
		stall_sync  Issue Stall Reasons (Synchronization)  1.54%   1.83%   1.63%
		stall_other  Issue Stall Reasons (Other)   4.31%  5.71%  4.88%
		stall_constant_memory_dependency Issue Stall Reasons (Immediate constant) 12.64% 14.13%  13.43%
		stall_pipe_busy Issue Stall Reasons (Pipe Busy) 0.62%  0.90%   0.75%
		shared_efficiency Shared Memory Efficiency14.29%  14.29% 14.29%
		inst_fp_32  FP Instructions(Single) 2528  2528 2528
		inst_fp_64  FP Instructions(Double)    0       0      0
		inst_integer Integer Instructions       32448     32448      32448
		inst_bit_convert  Bit-Convert Instructions     0      0       0
		inst_control  Control-Flow Instructions   3136    3136    3136
		inst_compute_ld_st  Load/Store Instructions    6688    6688    6688
		inst_misc     Misc Instructions   4352       4352    4352
	    inst_inter_thread_communication Inter-Thread Instructions 0    0   0
		issue_slots  Issue Slots      2608     2608        2608
		cf_issued    Issued Control-Flow Instructions    288   288   288
		cf_executed  Executed Control-Flow Instructions  288  288    288
		ldst_issued Issued Load/Store Instructions      1168  1168  1168
		ldst_executed  Executed Load/Store Instructions 768  768   768
		atomic_transactions  Atomic Transactions   0      0      0
		atomic_transactions_per_request  Atomic Transactions Per Request    0.0    0.0   0.0
		l2_atomic_throughput   L2 Throughput (Atomic requests)  0.00B/s  0.0B/s  0.0B/s
		l2_atomic_transactions  L2 Transactions (Atomic requests)   0     0    0
		l2_tex_read_transactions   L2 Transactions (Texture Reads)  384   384  384
		stall_memory_throttle   Issue Stall Reasons (Memory Throttle)  0.74% 0.88%  0.80%
		stall_not_selected    Issue Stall Reasons (Not Selected)     1.10%  1.65%    1.40%
	    l2_tex_write_transactions   L2 Transactions (Texture Writes) 16 16 16
		flop_count_hp   Floating Point Operations(Half Precision)   0    0  0
		flop_count_hp_add  Floating Point Operations(Half Precision Add)  0   0    0
		flop_count_hp_mul  Floating Point Operation(Half Precision Mul)   0    0   0
		flop_count_hp_fma  Floating Point Operations(Half Precision FMA)  0   0  0
		inst_fp_16     HP Instructions(Half)     0           0           0
		sysmem_read_utilization   System Memory Read Utilization   Idle (0)  Idle (0)  Idle (0)
		sysmem_write_utilization   System Memory Write Utilization Low (1) Low (1)  Low (1)
		sm_activity    Multiprocessor Activity  1.46%   2.19%    2.01%
		achieved_occupancy   Achieved Occupancy  0.238931  0.245158  0.243207
		executed_ipc    Executed IPC    0.986040    1.074583    1.030250
		issued_ipc     Issued IPC    0.994565    1.085651    1.040111
		issue_slot_utilization   Issue Slot Utilization  22.15%  24.18%  23.16%
		eligible_warps_per_cycle    Eligible Warps Per Active Cycle    0.872845  1.201177  1.128289
		tex_utilization    Unified Cache Utilization     Low (1)     Low (1)     Low (1)
		l2_utilization      L2 Cache Utilization   Low (1)  Low (1)  Low (1)
		shared_utilization   Shared Memory Utilization     Low (1)   Low (1)   Low (1)
		ldst_fu_utilization   Load/Store Function Unit Utilization   Low (1)   Low (2)   Low (1)
		cf_fu_utilization    Control-Flow Function Unit Utilization   Low (1)   Low (1)   Low (1)
		special_fu_utilization     Special Function Unit Utilization  Idle (0)  Idle (0)  Idle (0)
		tex_fu_utilization Texture Function Unit Utilization   Low (1)   Low (2)   Low (1)
		single_precision_fu_utilization   Single-Precision Function Unit Utilization Low (2) Low (2) Low (2)
		double_precision_fu_utilization  Double-Precision Function Unit Utilization Idle (0) Idle (0) Idle (0)
		flop_hp_efficiency  FLOP Efficiency(Peak Half)   0.00%    0.00%    0.00%
		flop_sp_efficiency   FLOP Efficiency(Peak Single) 0.01% 0.01%    0.01%
		flop_dp_efficiency   FLOP Efficiency(Peak Double)  0.00%   0.00%    0.00%
		dram_read_transactions   Device Memory Read Transactions    0     8     0
		dram_write_transactions  Device Memory Write Transactions   0     4      0
		dram_read_throughput   Device Memory Read Throughput  0.00000B/s  91.644MB/s  0.00000B/s
		dram_write_throughput   Device Memory Write Throughput  0.00000B/s  45.685MB/s  0.00000B/s
		dram_utilization   Device Memory Utilization Idle (0) Low (1) Idle (0)
		half_precision_fu_utilization Half-Precision Function Unit Utilization Idle (0) Idle (0) Idle (0)
		ecc_transactions      ECC Transactions   0      0      0
		ecc_throughput   ECC Throughput  0.00000B/s  0.00000B/s  0.00000B/s


5. 
下面这篇文章对于nvprof的几个metric给出了比较详细的解释：
http://blog.csdn.net/yu132563/article/details/60881163

对于可视化的profiler，可以参考如下博文：
http://blog.csdn.net/kkk584520/article/details/9490233



## PTX:

https://book.2cto.com/201409/46640.html



## ptxas是什么？

nvcc -Xptxas –v acos.cu 

ptxas info : Compiling entry function 'acos_main' 

ptxas info : Used 4 registers, 60+56 bytes lmem, 44+40 bytes smem, 20 bytes cmem[1], 12 bytes cmem[14] 

这里对上例进行一个简单的解释，smem表示共享存储器，这个地方它被分成了两个部分，第一个表示总共声明的共享存储器大小，后者表示系统在存储段中分配的数据总量：共享存储器中的device函数参数块和局部存储器中的线程索引信息。cmem表示常量存储器的使用情况，这里就是使用了一个20bytes的变量和一个长度为14的单位12byte的数组.
上面是从网上看到一个结果和对结果的的解释，感觉不太对，我计算过了smem加号前面的大小等于声明的sharememory的大小加上核函数参数数量乘以每个变量的字节数，后面的就不清楚是怎么算出来的了，后面对cmem的解释可能是错误的，我定义了__device__ __constant__ int cu_voiinf[6];        __device__ __constant__ int cu_phainf[6];但显示的是 72 bytes cmem[0], 148 bytes cmem[1]，所以对cmem可能不正确。




warp深度解析：

下面这个blog分析的非常好：

http://blog.163.com/wujiaxing009@126/blog/static/71988399201701224540201/





