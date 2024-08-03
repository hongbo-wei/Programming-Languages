#include"stdio.h"
#include"math.h"
int main()
{
	printf("Enter an opsitive integer less than 200: ");
	int n,m,i,flag;    
	scanf("%d",&n);
	if(n>0&&n<200)
	{
		for(n;n>1;n--)
		{
		 m=pow(2,n)-1;
		 i=2;flag=0;
		 for(;i<sqrt(m);i++)
	 	{
		 if (m%i==0){flag=1;break;}
		 }
		 if(flag==0)printf("m=%d\n",m);
		}
		
	}
	else
	printf("Wrong input\n");
	return 0;
} 