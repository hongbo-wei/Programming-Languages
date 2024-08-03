#include"stdio.h"
int main()

{   void copyString(char fun[]);
    char a[40];
    printf("Enter a string: ");
	gets(a);
	printf("String 'a' is: ");
	puts(a);
	copyString(a);
	return 0;
} 

void copyString(char fun[])
{
    char b[40],*p1,*p2;
	p1=fun,p2=b;
	for(;*p1!='\0';p1++,p2++)
		*p2=*p1;
	*p2='\0';
    printf("String 'b' is: %s\n",b);
}