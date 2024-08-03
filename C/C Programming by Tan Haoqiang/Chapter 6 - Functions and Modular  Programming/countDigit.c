#include"stdio.h"

int countDigit(int n, int d)
{
    int count=0;
	if(n<0)n=-n;
	for(;n>0;n=n/10)  if(n%10==d)count++;	
	return count;
}

int main()
{
	int n,d;
	scanf("%d %d",&n,&d);
	printf("Number of digit %d in %d is %d\n",d,n,countDigit(n,d));
	
	return 0;
}