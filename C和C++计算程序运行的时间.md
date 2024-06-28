```C++
#include <time.h>
clock_t start,end;
start = clock();
//需要测试运行时间的程序段
end = clock();
```
clock()函数： 得到从程序启动到此次函数调用时累计的毫秒数。 end-start就是程序段的运行时间。输出即得到程序段调用时累计的毫秒数。

CLOCKS_PER_SEC是标准c的time.h头函数中宏定义的一个常数，表示一秒钟内CPU运行的时钟周期数，用于将clock()函数的结果转化为以秒为单位的量，但是这个量的具体值是与操作系统相关的。

```C++
cout<<(double)(end-start)/CLOCKS_PER_SEC;
```
