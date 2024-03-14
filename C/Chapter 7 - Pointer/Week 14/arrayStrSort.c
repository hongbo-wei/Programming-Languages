#include <stdio.h>
#include <string.h>
int main()
{	void sort(char str[][20],int n);
	void print(char str[][20],int n);	
	char str[5][20];
	int n=5,i;
	printf("Note: Press 'Enter' for next string\n");
	printf("\nEnter 5 stings:\n\n");
	for(i=0;i<n;i++)
		gets(str[i]);
	sort(str,n);
	printf("\nAfter sort:\n\n");
	print(str,n);
	return 0;
}

void sort(char str[][20],int n)	
{
	char temp[20];
	int i,j;
	for(i=0;i<n;i++)	
	{	
		for(j=i+1;j<n;j++)
			if(strcmp(str[i],str[j])>0)
		{
			strcpy(temp,str[i]);
			strcpy(str[i],str[j]);
			strcpy(str[j],temp);
		}
	}
}
	
void print(char str[][20],int n)
{
	int i;
	for(i=0;i<n;i++)
	puts(str[i]);
}

