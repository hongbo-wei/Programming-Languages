#include "stdio.h"
int main()
{
	int n;
	printf("Enter an integer: \n");
	scanf("%d",&n);
	if(n%105==0)
	printf("����ֵ��ͬʱ��3��5��7����\n");
	else if(n%15==0)
    printf("����ֵ��ͬʱ��3��5����\n");
    else if(n%21==0)
    printf("����ֵ��ͬʱ��3��7����\n");
    else if(n%35==0)
    printf("����ֵ��ͬʱ��5��7����\n");
    else if(n%3==0)
    printf("����ֵֻ�ܱ�3����\n");
    else if(n%5==0)
    printf("����ֵֻ�ܱ�5����\n");
    else if(n%7==0)
    printf("����ֵֻ�ܱ�7����\n");
    else
    printf("����ֵ���ܱ�3��5��7����һ��������\n");
	return 0; 
    
} 