#include "stdio.h"
int main()
{
	int a[3][4]={
		1,2,3,4,9,8,7,6,-10,10,-5,2
	},r,c,max=a[0][0],row,column;
	for(r=0;r<=2;r++)
	   for(c=0;c<=3;c++)
	   if(a[r][c]>max)
	   {
   		max=a[r][c];
   		row=r;
   		column=c;
   	}
	printf("max=%d,row=%d,column=%d\n",max,row,column);
	return 0;
	
}