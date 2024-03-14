#include"stdio.h"
int main()
{
	int s[8]={54,45,36,81,72,18,63,27};
	int min,i,j,t;
	
	for(i=0;i<7;i++)
	{
		min=i;
		for(j=i+1;j<8;j++)if(s[j]<s[min]) min=j;
		t=s[i];
		s[i]=s[min];
		s[min]=t;
		for(j=0;j<8;j++)printf("%d ",s[j]);
		printf("\n");
	}
	
	printf("\nFinal result is:\n");
	for(i=0;i<8;i++)printf("%d ",s[i]);
	
	printf("\n");
	return 0;
}