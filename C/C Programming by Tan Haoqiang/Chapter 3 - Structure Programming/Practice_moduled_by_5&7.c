#include <stdio.h>
int main()
{
	printf("Enter a number: \n");
	int x;

	scanf("%d",&x);
	if(x%5==0 || x%7==0)
	printf("Yes, it is the dad of 5 or 7\n");
	
	else printf("No, it isn't the dad of 5 or 7\n");
	
	return 0;
}
