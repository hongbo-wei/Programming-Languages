#include "stdio.h"
#include "math.h"
int main () 
{
	float a,b,c,disc,root1,root2;
	printf("Enter the value of a, b, c of equation ax^2+bx=c=0: \n");
	scanf("%f%f%f",&a,&b,&c);
	disc=sqrt(b*b-4.0*a*c);
	if(disc>=0)
	{
	root1=(-b+disc)/2.0*a;
	root2=(-b-disc)/2.0*a;
	printf("root1=%f\nroot2=%f\n",root1,root2);
	}
	
	else
	printf("This equation has no real roots\n");
	return 0;
}