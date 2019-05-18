## CH 3 迅速掌握MPI

### Run
编译：mpicxx xx.cpp
执行：mpiexec -n 数字 可执行文件 参数

### 固定的开头结尾
```
#include <mpi.h>

int main(int argc, char *argv[]){
    // MPI Common Head
    int my_rank, comm_sz;
    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &my_rank);
    // 保存常量值：通信子中的进程标识号
    MPI_Comm_size(MPI_COMM_WORLD, &comm_sz);
    // 保存常量值：通信子中的进程数量
    MPI_Status status;

    // MPI Common Tail
    MPI_Finalize();
    return 0;
```

### Send,Recv
* 原理：FIFO
Send不可超越数组范围，Recv基于阻塞
* 基本
```
MPI_Send(&A[beginRow * n + 0], each_row * n, MPI_INT, i + 1, 1, MPI_COMM_WORLD);
// 指针，多少个，类型（MPI_Datatype的成员），to，编号，world
MPI_Recv(&C[beginRow * n + 0], each_row*n, MPI_INT, i + 1, 3, MPI_COMM_WORLD, &status);
// 指针，多少个，类型，from，编号，world，&status
```
&status用来获得source和tag
* Recv any
```
MPI_Recv(&C[beginRow * n + 0], each_row*n, MPI_INT, MPI_ANY_SOURCE, MPI_ANY_TAG, MPI_COMM_WORLD, &status);
```



### Isend，Irecv
非阻塞的send和recv搭配wait
最后多一个handle=&recv_handle或者&send_handle
wait是针对handle插入阻塞
MPI_WAIT(&status, &recv_handle)


### Scatter，Gather
```
MPI_Scatter(发送指针, 发送给每个数量, 发送类型, 接收指针, 接收数量, 接收类型, 发送方, MPI_COMM_WORLD);
// 发，收，谁发，所以每个进程都有一个

MPI_Gather(发送指针, 每个发送的数量, 发送类型, 接收指针, 接收每个的数量, 接收类型, 接收方, MPI_COMM_WORLD);
// 发，收，谁收，所以每个进程都有一个

MPI_Allgather(发送指针, 每个发送的数量, 发送类型, 接收指针, 接收每个的数量, 接收类型, MPI_COMM_WORLD);
// 类似的，没有接收方
```

### Bcast
```
MPI_Bcast(发送指针, 发送数量, 发送类型, 发送方, MPI_COMM_WORLD);
```

### Ssend，SendRecv
Ssend：强制阻塞
SendRecv：等于一个send一个recv，参数是两者之和

### Reduce
规约运算，可以用于全局树状求和
```
MPI_Reduce(from, to, 几个, 数据类型, 运算符, 结果送往进程号, MPI_COMM_WORLD);
```
收集方只是收集所有的from包括自己，按给的数顺序匹配是哪一次reduce；发送方的to没用
```
MPI_Allreduce(from, to, 几个, 数据类型, 运算符, MPI_COMM_WORLD);
```
这下to就有用了，大家都可以收到

### Split
MPI_Comm_split：划分通信域
```
MPI_Comm_split(MPI_COMM_WORLD, 通信域标识符color, my_rank, 新的通信域名字&rowcomm);
// 然后就可以用&rowcomm代替MPI_COMM_WORLD，作为一个局部通信域
```

### get count
MPI_Get_count(&status, recv_type, &count)
MPI_Get_address(&a, &a_shifted)

### Time
MPI_WTime()
MPI_Barrier()

### Struct
MPI_Type_create_struct
MPI_Type_commit

### 优化
很重要，要考
0.最简单，能发连续的就连续的
1.MPI_Pack
2.打包成结构体，明天细看