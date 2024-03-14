#include"stdio.h"
#include"string.h"
int main()
{
	char str[100],str2[100][100];
	int r,i,c1=0,c2=0,c3=0;
	gets(str);
	for(i=0;i<strlen(str);i++)
	{
		if(str[i]>='A' &&str[i]<= 'Z')
		{str2[0][c1]=str[i];c1++;}
		else if(str[i]>='a' &&str[i]<= 'z')
	    {str2[1][c2]=str[i];c2++;}
	    else if(str[i]>='0' &&str[i]<= '9')
		{str2[2][c3]=str[i];c3++;}
	}

	for(r=0;r<=2;r++)
	printf("\n %s \n",str2[r]);
}