#include <stdio.h>     
int main()                 //��Ŀ�� 1-1/2+1/3-1/4+��+1/99-1/100 
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
		sum=sum+t;  //��һ������Ϊ sum=1+(-1/2) �ڶ������� sum=1+(-1/2)+1/3 
		d=d+1;
	}
	printf("The result is %f\n",sum); //��ӡ�����ս�� 
	return 0;
} 