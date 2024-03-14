#include "stdio.h"
int n,p;
int power(int n,int p)
{
	int r;
	if(p==0)r=1;
	else
	{
	r=n*power(n,p-1);
	}
	return r;
}

int main() 
{
	printf("Enter an integer and its power: ");
	scanf("%d %d",&n,&p);
	printf("Result is %d\n",power(n,p));
}