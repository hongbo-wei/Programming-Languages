#include"stdio.h"
int main()
{
	int circle(int n);
	int n;
	printf("Enter an integer: ");
	scanf("%d",&n);
	printf("Number Left: %d\n",circle(n));
	return 0;
} 

int circle(int n)
{
	int circle[100],i,s=0,count=1,*p=circle;
	for(i=0;i<n;i++)
	{
		*p=i+1;
		printf("%d ",*p); 
		p++;
	}
	printf("\n");
	
	while(n>1)
	{
		if(count==3)
		{
			printf("Number Deleted: %d\n",circle[s]);
			for(i=s;i<n;i++)
			{
			circle[i]=circle[i+1];
			}
		count=1;
		n--;
		}
		else
		{
			count++;
			s++;
		} 
		if(s==n)s=0;
	}
		return circle[0];
}

