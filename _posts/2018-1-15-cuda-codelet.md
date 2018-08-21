---
layout:     post
title:      CUDA-有用的代码段
keywords:   new-feature
category:   CUDA
tags:		[CUDA编程]
---


# 获取SM号的内嵌汇编代码：

    __device__ unsigned int get_smid(void) {
        unsigned int ret;
        asm("mov.u32 %0, %smid;" : "=r"(ret) );
        return ret;
    }


#  用于块间同步的代码：

            // thread_index_inBlock代表块内的1维线程号；block_x代表块号（第几块）。
            //global_state_in和out都是global-mem。

                    if (thread_index_inBlock == 0){
                         global_state_in[block_x] = 1;
                    }
             
                    if (block_x == 0){
                            if (thread_index_inBlock < BLOCK_NUM){
                                while (global_state_in[thread_index_inBlock] != 1)
                                    {};
                             }
             
                         __syncthreads();
             
                         if (thread_index_inBlock < BLOCK_NUM){
                             global_state_out[thread_index_inBlock] = 1;
                         }
                    }
             
                    if (thread_index_inBlock == 0){
                        while (global_state_out[block_x] != 1){};
                    }
                    __syncthreads();

            解释：
            （1）	若块内线程号为0，则in为1；
            （2）	若块号为0：
                （a）	检查in数组是不是都为1，否则等；//保证（1）做完。
                （b）	块内同步；
                （c）	置out为1；
            （3）	若块内线程号为0，则检查out数组是不是都是1，否则等；//保证（2）做完。
            （4）	块内同步；


