#include"stdio.h"
int main(int argc, char *argv[])
{
	char str[100],nstr[20];
	printf("Enter a string no longer than 8 words: ");
	gets(str);
	void arostic(char str[],char nstr[]);
	arostic(str,nstr);
	puts(nstr);
//	char *ns=arostic(str,nstr);
//	printf("New word is: %s\n",ns);
	return 0;
}

void arostic(char str[],char nstr[])   //return pointer: char *arostic() 
{
	int i;
	char *p=nstr;
	char *np=nstr;
	for(i=0;str[i]!='\0';i++)
	{
		if(str[i]==' ')
		{
			*p=str[i-1];
			p++;
		}
	}
	*p=str[i-1];   //Last word
	*(p+1)='\0';   //End string
//	return np;
}
