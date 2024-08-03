#include"stdio.h"
int main()
{
	char c1[6]="China";
	char c2[6]=" No.1";
	int i=0,j=0;
	while(c1[i]!='\0')i++;
	while(c2[j]!='\0')
	{
		c1[i+j]=c2[j];
		j++;
	}
	c1[i+j]='\0';
 
	puts(c1);
}