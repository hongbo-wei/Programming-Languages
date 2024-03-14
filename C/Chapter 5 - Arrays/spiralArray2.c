#include"stdio.h"
int main()
{
  printf("Input number: ");
  int n;
  scanf("%d",&n);
  int array[100][100];
  int row,column,i=1;
  for(row=0;row<n;row++)
  {
if(row==0)
   {for(column=0;column<n;column++)
       {
        array[row][column]=i;
        i++;
        }
   }
else if(row>=1&&row<(n-1))
   {
    for(;row<(n-1);row++)
    {
   array[row][0]=4*(n-1)-(row-1);
   array[row][n-1]=n+row;
    }
     }
else
     {
      for(column=n-1,i=0;column>=0;column--)
      {
    	array[n-1][column]=2*n-1+i;
       i++;
      }
     }
  }
   for(row=0;row<n;row++)
   {
   	for(column=0;column<n;column++)
   	 printf("%3d",array[row][column]);
   	 printf("\n");
   }
}