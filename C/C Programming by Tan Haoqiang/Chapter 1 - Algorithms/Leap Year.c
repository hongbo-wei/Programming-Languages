#include <stdio.h>
int main()
{
	int y;
	y=2000;
	
	while(y<=2500)
	{
    if((y%4==0 && y%100!=0) || y%400==0)
	{
	    printf("%d is a leap year\n",y);
		y=y+1;
	}
	else 
	{
		printf("%d is not a leeap year\n",y) ;
		y=y+1;
	}
	}
	
	return 0;
}