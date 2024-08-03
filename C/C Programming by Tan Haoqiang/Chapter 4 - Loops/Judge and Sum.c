#include "stdio.h"
int main()
{
	int n,sum=0;
	printf("Enter an integer: \n");
	scanf("%d",&n);
	if (n%2==0)
	{
		printf("Number %d is even\n",n);
		while(n>0)
		{
			sum=sum+n;
			n=n-2;
		}
		printf("sum is %d\n",sum);
	}
	else
	{
		printf("Number %d is odd\n",n);
		while(n>0)
		{
			sum=sum+n;
			n=n-2;
		}
		printf("sum is %d\n,sum");	
	}
}
