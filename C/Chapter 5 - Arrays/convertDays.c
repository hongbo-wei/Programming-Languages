#include "stdio.h"
int main()
{
static int  month_tab[2][13]= 
    { {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31},
	  {0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31} };
	int i,year,month,day,sumDay=0;
	printf("Enter Year Month Day with number in form Y M D: ");
	scanf("%d %d %d",&year,&month,&day);
	if(year%4==0&&year%100!=0||year%400==0)  
	i=1;
	else
	i=0;
	
	for(month;month>0;month--) 
	sumDay=sumDay+month_tab[i][month-1];
	sumDay=sumDay+day; 
	
	printf("sumDay is %d\n",sumDay);
	return 0;
}
