#include "stdio.h"
#include "string.h"
int main()
{
	char str[30];
	gets(str);
	int len=strlen(str),flag=1,i;
	for(i=0;i<len/2;i++)
	{
		if(str[i]!=str[len-1-i])flag=0;
		
	}
	if(flag==1)printf("The order is the same as the inverted sequence\n");
	else if(flag==0) printf("The order is NOT the same as the inverted sequence\n");
}