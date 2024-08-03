#include"stdio.h"
int factorial(int n)
{
	int z;
	if(n==0||n==1)
	z=1;
	els e
	z=n*factorial(n-1);
	return z;
}

int facsum(int n)
{
	int m=1,z=0;
	for(;m<=n;m++)
	z=z+factorial(m);
	return z;
}

int main()
{
	printf("Input number n: ");
	int n,z;
	scanf("%d",&n);
	z=facsum(n);
	printf("%d\n",z);
	return 0;
}