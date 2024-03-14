#include"stdio.h"
int main()
{
	void delSpace(char *p);
	char str[100];
	printf("Enter a string: ");
	gets(str);          // Input string
	delSpace(str);   // Call function
	printf("Space deleted: ");
	puts(str);          //Output string
	printf("\n");
	return 0;
}

void delSpace(char *p)
{
	int i;
	for(;*p!='\0';p++)
	{
		if(*p==' ')
		{
			for(i=0;*(p+i)!='\0';i++)
				*(p+i)=*(p+i+1);
		}
	}
}