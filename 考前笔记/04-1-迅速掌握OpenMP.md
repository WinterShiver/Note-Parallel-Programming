## CH 5-1 迅速掌握OpenMP

### 基本概念
* 控制更宏观，不是显式指定每个线程做什么，只是粗略标注这块可以并行
* 对串行程序进行增量型并行化
* 自带barrier


### Run
编译：g++ -fopenmp
执行：可执行文件 参数

### 固定的开头结尾
```
#include <mpi.h>
```

### 最简单的并行
```
// 以下代码所有都过一遍，线程数=核数
#pragma omp parallel
// 以下代码所有都过一遍，线程数指定
#pragma omp parallel num_threads(thread_count)
```
执行模式：主线程一直在跑，到对应指令了，创建count-1个线程开始一起做，做完之后再exit掉其他的，所以可能不按顺序

### 线程信息
int my_rank = omp_get_thread_num()
int thread_count = omp_get_num_threads()

### 通信
```
// 以下代码所有都过一遍+避免竞争
#pragma omp critical
```
**优化**：critical相当于用来通信，其执行效率相当于串行，所以不要放复杂的东西
```
// 利用规约完成求和
#pragma omp parallel num_threads(thread_count) reduction(+: global_sum)
```

### for
```
// 并行for循环
#pragma omp parallel for
```
* 看起来很美，但循环次数必须固定，只能对操作数进行正常的数学操作，操作数必须是整型或者指针，程序不能有很多出口（break，return...）
* 最关键：不处理数据依赖
  * 串行循环和并行循环
  * 变量重命名机制

### 共享作用域和私有作用域
* 概念：全部线程都可访问；只能被一个线程访问
* 默认：共享

```
// 创建私有作用域
#pragma omp parallel num_threads(thread_count) private(factor)
```
实质相当于重新定义了私有变量，所以记得赋值
```
// 创建私有作用域
#pragma omp parallel num_threads(thread_count) firstprivate(factor)
```
firstprivate继承之前的值
lastprivate修改值传回去，只能用于parallel for（可想而知，这个是用来最后统一结果的）
```
// 创建私有作用域
#pragma omp parallel num_threads(thread_count) default(none) reduction(xxx) private(xxx) shared(xxx)
```
哪些共享哪些不共享
```
#pragma omp atomic
```
一句话的临界区，更方便

### 循环划分和调度
* 问题：按块分割会造成不均匀，每趟循环用时不一定一样
* 解决：块划分改为细粒度划分，每趟循环动态分配给线程
* 静态schedule：指定块大小之后还是一轮分配好
```
#pragma omp parallel num_threads(thread_count) reduction(+: glo_sum) schedule(static,1)
```
* schedule(dynamic, chunksize=1)：先定好块大小（这么多个），再随完随分，稍微智能一点，系统开销稍大
* schedule(guided, chunksize=1)：随完随分，块大小越分越小，很智能但系统开销很大
* 事先知道每趟平稳递增or递减，建议static，chunksize=小
* 事先不能确定每趟开销：schedule(runtime)自动测试选取

### barrier
#pragma omp barrier
任何其他指令后面nowait去barrier
常见优化：防止总同步，前面一波nowait，最后再barrier

### lock
omp_lock_t
omp_init_lock(&lock)
omp_set_lock(&lock)
omp_unset_lock(&lock)
omp_destroy_lock(&lock)

### 优化思路
一般的好看出来的就不说了

#### 排序
* 奇偶交换排序
* 原理：只能跟邻居换，一轮一轮查
* 思路：内部循环并行，1和2换与3和4换并行，不同轮次之间自带barrier可以保证不错
* 进阶：创建线程很费时，防止多次parallel，先parallel再for
```
#pragma omp parallel num_threads(thread_count)
for1{
    #pragma omp for
    for2{}
}
```
#### 生产者-消费者
消息队列，多人push一人pop
针对critical进行优化，但又不能不用critical
