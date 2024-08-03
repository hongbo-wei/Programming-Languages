#include"stdio.h"
int main()
{
  void fun_sort(int *a,int *b,int *c); 
  int n1,n2,n3,max;
  printf("Enter 3 integer number: ");
  scanf("%d %d %d",&n1,&n2,&n3);
  int *a=&n1,*b=&n2,*c=&n3;
  fun_sort(a,b,c);
  printf("%d %d %d",*a,*b,*c);
  printf("\n");
  return 0;
} 

void fun_sort(int *a,int *b,int *c) 
{
    int temp;
	if(*a>*b)
	{
		temp=*a;
		*a=*b;
		*b=temp;
	}
	if(*b>*c)
	{
		temp=*b;
		*b=*c;
		*c=temp;
	}
	if(*a>*b)
	{
		temp=*a;
		*a=*b;
		*b=temp;
	}
}