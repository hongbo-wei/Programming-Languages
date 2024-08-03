#include "stdio.h"
int main()
{
	int a[6]={1,2,3,4,5,6},b[6]={1,2,3,4,5,6},i,sum[6],sub[6];
	for(i=0;i<6;i++)
	{
	sum[i]=a[i]+b[i];
	printf("%d ",sum[i]);}

printf("\n");
	
	for(i=0;i<6;i++)
	{
	sub[i]=a[i]-b[i]; 
	printf("%d ",sub[i]);}
	
	printf("\n");
	return 0;
} 