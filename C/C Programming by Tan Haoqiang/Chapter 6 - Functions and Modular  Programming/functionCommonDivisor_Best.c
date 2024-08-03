	#include"stdio.h"
	
	int main()
	{
		int gcd (int x,int y);
		int x,y;
		printf("Input intergers x y: \n");
		scanf("%d %d",&x,&y);
		printf("Their largest common factor is: %d\n",gcd(x,y));
		
	}
	
	int gcd(int x,int y)
	{
		int c,replace;
		if(y>x)
		{
			replace=x;
			x=y;y=replace; 
		}
		c=x%y;
	    if(c==0) return y;
		else
		{
		if(y%c==0)return c;
	    else return y%c;
		}
	} 
