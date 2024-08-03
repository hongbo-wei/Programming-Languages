#include"stdio.h"
int main()
{
  printf("Input number: ");
  int n;
  scanf("%d",&n);
  int spiral[n][n];
  int row,column,i=1;
 for(row=0;row<n;row++)
  {
       for(column=0;column<n;column++)
  	    {
	  	    spiral[0][column]=i;
	      	i++;
        }
      for(row=1;row<n;row++)
  		{
		 spiral[row][n-1]=i;
		 i++;
		  }
	  for(column=n-2;column>=0;column--)
  	  	{
	  	  	spiral[n-1][column]=i;
	  	  	i++;
	  	  }
	  for(row=n-2;row>0;row--)
	  {
  		spiral[row][0]=i;
  		i++;
  	}
  }	
 for(row=0;row<n;row++)
  {
  	for(column=0;column<n;column++)
  	{printf("%d ", spiral[row][column]);}
  	printf("\n");
  }
}
