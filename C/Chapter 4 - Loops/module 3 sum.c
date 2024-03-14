#include  "stdio.h"
int main()
{
	int i=99,s=0,n=1;
	loop:if(i>1)
	{
		printf("%d ",i);
		if(n%4==0)
		{
		printf("\n");	
		}
		s=s+i;
		i=i-3;
		n++;
		goto loop;
	}
	printf("sum=%d\n",s);
	return 0;
}