## 迅速掌握CUDA

### 基本概念

### 硬件
并行程度高
GeForce：显卡，Tesla：用于服务器

### Run
编译执行：nvcc hello.cu arch=compute_35, code=sm_35
执行：可执行文件
nvcc把CUDA部分变成device code，然后编译成二进制码，和C语言的二进制码一起放在异构平台跑
GPU只负责高度并行部分

### 程序结构
* 声明在GPU上运行的函数
  * \_\_global\_\_（主机调用，GPU上执行）
  * global：内核函数，返回void，定义参数指定如何启动
  * host：主，主，device：G，G
* （进入主函数以后）获得GPU硬件信息
  * threadIdx.x
  * cudaGetDeviceCount()
  * cudaGetDevice()
  * cudaSetDevice()
  * cudaGetDeviceProperties()
* GPU函数调用的错误处理
  * 返回类型cudaError_t：描述成功or失败信息
  * HandleError（要执行的函数）
* copy参数fromCPUtoGPU
  * cudaMelloc((void**)&name, size)
  * cudaMemcpy(to, from, size, cudaMemcpyHostToDevice)
  * H2D，H2H，D2H，D2D
* 调用GPU上函数
  * foo<<<参数>>>结果
  * 具体：一个核对应一个线程网格
    概念：thread grid（线程块的网格）, thread block（线程的网格）
    * gridDim.x or y or z, blockDimx.x or y or z
    * blockIdx.x or y or z, threadIdx.x or y or z
    * index计算
* copy结果fromGPUtoCPU
  * cudaMemcpy(to, from, size, cudaMemcpyDeviceToHost)
* free GPU memory
  * cudaFree(name)

### 固定的开头结尾
```
#include <mpi.h>
```

### 线程的组织
以线程束组织（一般一束32）
执行，挂起（写入内存）
