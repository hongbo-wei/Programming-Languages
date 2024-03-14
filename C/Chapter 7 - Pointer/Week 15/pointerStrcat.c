#include"stdio.h"	
int main()
{
	void strlink(char *str1,char *str2);
	char str1[100],str2[100];
	printf("Input 1st string: ");
	gets(str1);
	printf("Input 2nd string: ");	
	gets(str2);
	strlink(str1,str2);
	printf("\nCombined: %s\n\n",str1);
	return 0;
}

void strlink(char *str1,char *str2)
{
	while(*str1!='\0')
		str1++;
	while(*str2!='\0')
	{
		*str1=*str2;
		str1++;
		str2++;
	}
	*str1='\0';
}
