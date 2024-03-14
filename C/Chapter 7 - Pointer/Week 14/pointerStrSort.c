#include <stdio.h>
#include <string.h>
int main()
{ 
	void sort(char *str[],int n);
	void print(char *str[],int n); 
	char str[5][50],*p[5];
 	int	n=5,i;
 	printf("Note: Press 'Enter' for next string\n");
 	printf("Enter 5 stings:\n");
 	for(i=0;i<n;i++)
 		{gets(str[i]);
		 p[i]=str[i];
 		}
 	printf("\nAfter Sorting:\n");
 	sort(p,n);
 	print(p,n);
 	return 0;
}
 
void sort(char *str[],int n) 
{	
	char *temp;
 	int i,j;
 	for(i=0;i<n-1;i++)  
 	{ 
  		for(j=i+1;j<n;j++)
		{if(strcmp(str[i],str[j])>0)
  			{temp=str[i]; str[i]=str[j]; str[j]=temp;}
		}
 	}
}

void print(char *str[],int n) 
{
	int i;
 	for(i=0;i<n;i++)
  	puts(str[i]);
}