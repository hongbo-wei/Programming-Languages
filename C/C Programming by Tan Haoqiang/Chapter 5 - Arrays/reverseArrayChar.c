#include"stdio.h"
#include"string.h"
int main()
{
	char str1[40]="I am from China";
	char str2[10][10]; 
	int i,row=0,column;
	
	for(i=0;i<strlen(str1);i++)
	{
	column=0;
	  while(str1[i]!=' ' && str1[i]!='\0')	
	  {
	  str2[row][column]=str1[i];
	  column++;
	  i++;
	  }
	str2[row][column]='\0';
	row++;
	}
	for(row=row-1;row>=0;row--)
	printf("%s ",str2[row]);
	
	printf("\n");
}
