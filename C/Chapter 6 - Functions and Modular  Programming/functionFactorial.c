#include"stdio.h"
int factorial(int n)
{
	int f;
	if(n==0||n==1)
	f=1;
	else
	f=n*factorial(n-1);
	return f;
}

int main()
{
	printf("Input number m and n (m>n): ");
	int m,n,z;
	scanf("%d %d",&m,&n);
	z=factorial(m)*factorial(n)/factorial(m-n);
	printf("%d\n",z);
	return 0;
}