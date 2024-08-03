#include"stdio.h"
int Fibo(int n)
{
	int i,j,z=0,f[20];
	f[0]=0,f[1]=1;
	for(i=1;i<=n;i++)
	{
	if(i==1)f[i]=1;
	else
	{f[i]=f[i-1]+f[i-2];}
	z=z+f[i];
	printf("%d\t",f[i]);
	if(i%5==0)printf("\n");
	}
	return z;
} 

int main()
{
	int n=20;
	printf("The sum of the first twenty Fibonacci numbers is %d\n", Fibo(n));
	
}
