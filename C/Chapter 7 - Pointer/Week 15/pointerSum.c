#include"stdio.h"
int main()
{
    void judge(int);float sum(int);
	void (*p1)(int)=judge;float (*p2)(int)=sum;
//	p1=judge;p2=sum;
	int n;
	printf("Enter a positive integer: ");
	scanf("%d",&n);
	(*p1)(n);
//	float r=();
//	r=(*p2)(n);
	printf("Sum: %4.2f\n",(*p2)(n));
	return 0;
}

void judge(int n)
{
	if(n%2==0) printf("Input even number\n");
	else printf("Input odd number\n");
}

float sum(int n)
{
	float r=0;
	while(n>0)
	{
		r+=1.0/n;
		n-=2;
	}
	return r;
}
