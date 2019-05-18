## CH 4 迅速掌握Pthreads

### 基础知识
共享内存编程，利用多个线程完成任务，控制这些线程

### Run
编译：gcc -lpthread
执行：可执行文件 参数

### 固定的开头结尾
```
#include <pthread.h>

type foo(some args){
    // 子线程执行
}

int main(){
    // 创建句柄，内容是线程ID和其他信息
    // 信息用来：1.确定是哪个线程，2.操作之
    pthread_t* thread_handles; 
    thread_handles = malloc(线程数*sizeof(thread_t));
    // 启动线程
    for(int i=0; i<线程数; i++){
        pthread_create(句柄=&thread_handles[i], NULL, 要执行的函数名=foo, (void*)i);
    }
    
    /* 主线程执行 */
    
    // 终止线程
    for(int i=0; i<线程数; i++){
        pthread_join(thread_handles[i], NULL);
    }
    // 释放句柄空间
    free(thread_handles);
    return 0;
}
```

### Create
```
pthread_create(句柄=&thread_handles[i], NULL, 要执行的函数名=foo, (void*)i);
```

### 使用共享内存的问题
* $\pi$问题：首先，各个线程的任务是没有相关性的，所以可以并行，具体操作是加同一个共享变量
* 问题：不一致性，竞争资源
  解决1：忙等，缺点：忙等也耗CPU，不值
  解决2：Mutex 互斥量
* 问题：控制线程访问顺序
  解决：Semaphore 信号量
* 问题：同步
  解决：Barrier
* 单链表member，insert，delete问题
  解决：读写锁，好于用互斥量控制读写

### Mutex
pthread_mutex_t sum_lock;
pthread_mutex_init(&sum_lock, NULL);
pthread_mutex_destroy(&sum_lock);
pthread_mutex_lock(&sum_lock);
pthread_mutex_unlock(&sum_lock);

### Semaphore
sem_t sum_sem;
sem_init(&sum_sem, 0, 初始值);
sem_destory(&sum_sem);
sem_post(&sum_sem); //解锁
sem_wait(&sum_sem); // 等解锁

### Barrier
pthread_barrier_init(&xx, NULL, 需要同步的线程数量)
destory
wait：所有线程在这同步

### rwlock
init(&xx, NULL)
destory
pthread_rwlock_rdlock
pthread_rwlock_wrlock
pthread_rwlock_unlock

