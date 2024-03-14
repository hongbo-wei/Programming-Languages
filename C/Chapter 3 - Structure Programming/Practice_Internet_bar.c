#include <stdio.h>
int main()
{
	printf("Enter your age: \n");
	
	int age;
	scanf("%d",&age);
	if(age>=18)
	printf("You are allowed to enter Internet bar\n");
	else
	printf("Guys under 18 are fobidden to enter\n");
	return 0;
	
}