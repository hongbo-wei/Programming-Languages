#include <stdio.h>
#include <string.h>
int main()
{	void sort(char *str[],int n);
	void print(char *str[],int n);	
	char *str[5]={
		"blue","yellow","red","black","green"
	};
	int n=5,i;
	sort(str,n);  
	print(str,n);
	return 0;
}

void sort(char *str[],int n)	
{	char *temp;
	int i,j;
	for(i=0;i<n-1;i++)		
	{	
		for(j=i+1;j<n;j++)
			if(strcmp(str[i],str[j])>0)
		{temp=str[i]; str[i]=str[j]; str[j]=temp;}
	}
}

void print(char *str[],int n)	
{	int i;
	for(i=0;i<n;i++)
		printf("%s\n",str[i]);
}
