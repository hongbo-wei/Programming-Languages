#include "stdio.h"
int main()
{
	int x,n,num[4],i,t;
	printf("Enter 4 digits number: "); 
	scanf("%d",&x);
	for(i=3;i>=0;i--)
	{
		n=x%10;
		x=(x-n)/10;
		
		num[i]=n;
		num[i]=(num[i]+9)%10;
	}
	
	for(i=0;i<2;i++)
	{
		t=num[i];
		num[i]=num[i+2];
		num[i+2]=t; 
	}
	
	for(i=0;i<4;i++)printf("%d",num[i]);
	printf("\n");
	return 0;
}