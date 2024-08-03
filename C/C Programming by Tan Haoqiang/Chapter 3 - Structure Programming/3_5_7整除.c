#include "stdio.h"
int main()
{
	int n;
	printf("Enter an integer: \n");
	scanf("%d",&n);
	if(n%105==0)
	printf("该数值能同时被3、5、7整除\n");
	else if(n%15==0)
    printf("该数值能同时被3、5整除\n");
    else if(n%21==0)
    printf("该数值能同时被3、7整除\n");
    else if(n%35==0)
    printf("该数值能同时被5、7整除\n");
    else if(n%3==0)
    printf("该数值只能被3整除\n");
    else if(n%5==0)
    printf("该数值只能被5整除\n");
    else if(n%7==0)
    printf("该数值只能被7整除\n");
    else
    printf("该数值不能被3、5、7任意一个数整除\n");
	return 0; 
    
} 