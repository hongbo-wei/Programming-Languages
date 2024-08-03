#include"stdio.h"
int judge(int n)
{
	int i,flag=1;
	if(n>2)
	{
		for(i=2;i<=n/2;i++) 
		{if(n%i==0)
		 {flag=0;break;}
		}   
    }
    else if (n==1||n==0) flag=0;
    return flag;
}
int prime(int n)
{
    for(;n>=2;n--)		
	{
    if(judge(n)==1)printf("%d Prime Number\n",n);
	}
}


int main()
{
	int n;
	scanf("%d",&n);
	if(judge(n)==0)printf("%d Not Prime Number\n",n); 
    prime(n);
}


