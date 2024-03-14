#include"stdio.h"
int main()
{
	char c1[6]=" No.1";
	char c2[6]=" ";
	int i=0;
	while(c1[i]!='\0')  //=while((c2[i++]=c1[i])!=0);
	{
		c2[i]=c1[i];
		i++;
	}
	c2[i]='\0';
 
	puts(c2);
}

/* #include"stdio.h"
#include"string.h"
int main()
{
	char c1[6]=" No.1";
	char c2[6]=" ";
	strcpy(c1,c2);
 
	puts(c1);
} */