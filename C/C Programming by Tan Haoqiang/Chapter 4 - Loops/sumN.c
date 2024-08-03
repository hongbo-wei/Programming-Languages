#include "stdio.h"
int main()
{
	float n=1,sum=0;
	while (n<=100)
	{
		sum=sum+1/n;
		n=n+2;
	}
	printf("sum=%10.4f\n",sum);
	return 0;

}