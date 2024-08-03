#include "stdio.h"
int main()
{
	int n,m,sum,sqaSum;
	printf("Enter a positive integer: \n");
	scanf("%d",&n);
	for(sum=0,sqaSum=0;n>=1;n/=10)
	{
		m=n%10;
		sum=sum+m;
		sqaSum=sqaSum+m*m;
	}
	printf("sum is %d, sqaSum is %d\n",sum,sqaSum);
	return 0;
}