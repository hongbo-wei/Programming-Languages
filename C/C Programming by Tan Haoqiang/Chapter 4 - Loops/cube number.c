#include  "stdio.h"
#include  "math.h"
int main()
{
	int od,td,hd,n;//od one digit ��λ����tdʮλ����hd��λ��
	for(n=100;n<=999;n++)
	{
		od=n%10;
		td=(n%100)/10;
		hd=(n%1000)/100;
		if(n==pow(od,3)+pow(td,3)+pow(hd,3))
		printf("%d\n",n);
		
	} 
	return 0;
}