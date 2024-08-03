#include "stdio.h"
int fun(int n)
{
	int s;
	if(n<0)printf("Wrong input\n");
	else if(n==0)s=0;
	else
	{
	s=n%10+fun(n/10);
	}
	return s;
}

int main() 
{   
    int n;
	printf("Enter an integer: ");
	scanf("%d",&n);
	printf("Fun result is %d\n",fun(n));
}