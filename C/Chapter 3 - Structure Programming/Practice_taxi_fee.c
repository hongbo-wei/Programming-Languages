#include <stdio.h>
int main()
{
	printf("Enter Taxi driving distance(km): \n");
	float d,m;
	m=6;
	scanf("%f",&d);
	if(d>3)
		{
		m=m+(d-3)*1.5;
		printf("Pay %.1f RMB\n",m); 
	}
	else
	printf("Pay 6 RMB\n");
	
	return 0;
} 


