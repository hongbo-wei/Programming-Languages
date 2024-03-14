#include"stdio.h"
int main()
{
	int r1=1,r2=1,sum=0,n,m=2;  //r1为第一个1个月的兔子数量，r2为第2个月的兔子数量 
	printf("Enter the pair of rabbit: ");
	scanf("%d",&n);
	if(n>=2)
		{
    while(sum<n) 
	{
		sum=r1+r2;
		r1=r2;
		r2=sum; 
		m+=1;
	}
	printf("It takes %d month\n",m);
        }
	else if(n==1)
	printf("At the very first day of the universe, there are already 1 pair of rabbit\n");
	else
    printf("It must be more than 0 pair\n");


   return 0;	 
}