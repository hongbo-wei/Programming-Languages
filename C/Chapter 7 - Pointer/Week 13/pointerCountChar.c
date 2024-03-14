#include"stdio.h"
int main()
{
	int countChar(char a[]);
	char a[40];
	printf("Enter a string: ");
	gets(a);
	printf("The length of string is: %d character(s).\n",	countChar(a));
	return 0;
}

int countChar(char a[])
{
	char *p=a;
	int i=0;
	for(;*p!='\0';p++,i++);
	return i;
}