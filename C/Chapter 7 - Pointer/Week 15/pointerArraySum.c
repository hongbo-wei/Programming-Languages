#include"stdio.h"
int main()
{
	void fun(int *a, int, int *even, int *odd);
	int a[8]={1,8,2,3,11,6,9,12};
	int n=8,sum_e=0,sum_o=0;
	int *even=&sum_e,*odd=&sum_o;
	fun(a,n,even,odd);
	printf("The sum of even numbers is: %d\n",*even);
	printf("The sum of odd numbers is: %d\n",*odd);
	return 0;
}

void fun(int *a, int n, int *even, int *odd)
{
	int i;
	for(i=0;i<n;i++)
	{
		if(a[i]%2==0)
		{
			*even+=a[i];
		}
		else
		{
			*odd+=a[i];;
		}
	}
}
