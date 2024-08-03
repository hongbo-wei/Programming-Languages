#include "stdio.h"
int main()
{
	printf("What day is today: \n"); 
	int d;
	scanf("%d",&d);
	if(d%5==4 || d%5==0)
	printf("Drying in day %d\n",d);
	else
	printf("Fishing in day %d\n",d);
	return 0;
}
