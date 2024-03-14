#include "stdio.h"
int main()
{
	int a[10]={10,9,8,7,6,5,4,3,2,1},i,j,t;
		for(j=0;j<9;j++)
	{
		for(i=0;i<10;i++)
	{if(a[i+1]<a[i])
		{
		t=a[i+1];
		a[i+1]=a[i];
		a[i]=t;
		}
	printf("%d ",a[i]);}
    printf("\n");
	}
	printf("\n"); 
	return 0;
}