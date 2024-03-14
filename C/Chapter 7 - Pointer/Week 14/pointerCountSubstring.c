#include"stdio.h"
#include"string.h"
int main()
{
	int countSubstring(char *str,char *sub);
	char str[100],sub[99];
	printf("Enter String: ");
	gets(str);
	printf("Enter Substring: ");
	gets(sub);
	printf("Substring appears %d times\n",countSubstring(str,sub));
	return 0;
}

int countSubstring(char *str,char *sub)
{
	int count=0,i,j;
	for(i=0;i<strlen(str);i++)
	{
		for(j=0;j<strlen(sub);j++)
		{
			if(str[i+j]!=sub[j])break;
		}
		if(j==strlen(sub))count++;
	}
	return count;
}

