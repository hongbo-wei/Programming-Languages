#include "stdio.h"
int main()
{

	printf("Enter twos numbers which refer to speed limitation and current speed to see whether there is a speeding punishment: \n"); 
	printf("Numbers should be greater than 0 and less than 100\n");
	float l,s,r;
    scanf("%f%f",&l,&s);
    r=s/l-1;
    
    if(r<0.1)
	printf("No speeding ticket Yep!\n") ;
	
    else if(r=0.1)
	printf("No speeding ticket Yep!\n") ;
	
	else if(r>0.1&&r<=0.5)
	printf("200 RMB Fine \n");
	
	else
	printf("Your Driving License Will Be Revoked\n");
    
    return 0;
}
