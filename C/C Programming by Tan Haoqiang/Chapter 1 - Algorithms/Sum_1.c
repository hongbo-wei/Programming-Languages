#include <stdio.h>     
int main()                 //题目求 1-1/2+1/3-1/4+…+1/99-1/100 
{
	int n,d;
	n=1;
	d=2;
	float t,sum;
	sum=1;
	while(d<=100)
	{
		n=-n;       //n = -1
		t=1.0*n/d;      //t = -1/2
		sum=sum+t;  //第一次运算为 sum=1+(-1/2) 第二次运算 sum=1+(-1/2)+1/3 
		d=d+1;
	}
	printf("The result is %f\n",sum); //打印出最终结果 
	return 0;
} 