#include"stdio.h"
#include"math.h"
int prime(int n)  //�������� 1�����򷵻� 0
{
	int i;
	for(i=2;i<sqrt(n);i++)    //n����ȥ��2,3...n-1
	{
		if(n%i==0) break;	
	}
	 if(i<sqrt(n))return 0;
	 else return 1;
} 

int main()
{
	int x,i,a;
	printf("Enter a positive integer less than 200: ");
	scanf("%d",&x);
	for (i=2;i<=x;i++)
	{
		a=pow(2,i)-1;  //2^n-1 
		if(prime(a)==1)
		{
			printf("%d\n",a);
		}
	}
} 