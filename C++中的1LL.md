两个整数相乘结果还是整数，因此就算赋值给long long还是会溢出。
```C++
// A program shows problem if we 
// don't use 1ll or 1LL 
#include <iostream> 
using namespace std; 
int main() 
{ 
	int x = 1000000; 
	int y = 1000000; 

	// This causes overflow even 
	// if z is long long int 
	long long int z = x*y; 

	cout << z; 
	return 0; 
}
```
>Output: -727379968
可以将x，y设为long long，也可以使用1LL (或1ll)。LL是long long的后缀，在大多数C/C ++实现中是64位的。所以1LL，是一个类型 long long 的1。
```C++
// C++ program to show that use of 1ll 
// fixes the problem in above code. 
#include <iostream> 
using namespace std; 
int main() 
{ 
	int x = 1000000; 
	int y = 1000000; 

	long long int z = 1LL*x*y; 

	cout << z; 
	return 0; 
} 
```
>Output: 1000000000000
