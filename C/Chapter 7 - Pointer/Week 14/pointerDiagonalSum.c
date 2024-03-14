#include"stdio.h"
int main()
{
	int sum1(int (*a)[6],int n);
	int sum2(int (*a)[6],int n);
	int Matrix[6][6],*p=Matrix[0],n=6,i=0;
	for(;i<n*n;i++)
	{
		*p=i+1;
		p++;
	}
	int (*a)[6]=Matrix;
	printf("1st Diagonal sum is %d\n2nd Diagonal sum is %d\n",sum1(a,n),sum2(a,n));
	return 0;
}
int sum1(int (*a)[6],int n)
{
	int sum1=0,i;
	for(i=0;i<n;i++)
	{
		sum1+=*(*(a+i)+i);
	}
	return sum1;
}
int sum2(int (*a)[6],int n)
{
	int sum2=0,i;
	for(i=0;i<n;i++)
	{
		sum2+=*(*(a+i)+(n-1-i));
	}
	return sum2;
}