#include "stdio.h"
void print (int rows)
{
	int i,j;
	for(i=1;i<=rows;i++)
	{
    	for(j=0;j<rows-i;j++)printf(" ");
		for(j=1;j<=2*i-1;j++)printf("*");
		printf("\n");
	}
	printf("\n");
}

int main()
{
	print(5);
}


/*  
    *
   ***
  *****
 *******
*********
*/