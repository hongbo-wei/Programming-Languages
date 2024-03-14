#include "stdio.h"
#include "math.h"
int main()
{
 int n,i,flag=1;
 printf("Enter a positive integer: \n");
 scanf("%d",&n);
 for(i=2;i<=sqrt(n);i++)
 {
  if(n%i==0)
  	{
	  flag=0;break;
    } 
 }
  if(flag==0)
  printf("Number %d is  NOT a prime number\n",n);
  else
  printf("Number %d is a prime number\n",n);  
  
  return 0;
}
