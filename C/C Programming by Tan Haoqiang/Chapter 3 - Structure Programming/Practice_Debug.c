#include <stdio.h>
int main()
{
printf("Enter your number: \n");
int x,y;
scanf("%d",&x);
if(x*x - 10>0){
	y = x*x;
	printf("y= %d\n",y);
}
else{
	y = -(x*x);
    printf("y= %d\n",y);
}

return 0;
}
