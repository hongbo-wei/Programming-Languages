#include"stdio.h"
int gcd(int x,int y)
{
	int f,iX=0,iY=0,arrayX[100],arrayY[100];
	for(f=1;f<=x;f++)
	{
	    if(x%f==0)
		{arrayX[iX]=f;
		iX++;
		}	
	}
	iX--;
	for(f=1;f<=y;f++)
	{
	    if(y%f==0)
		{arrayY[iY]=f;
		iY++;
		}	
	}
	iY--;
	int c,j,w=0,arrayCommon[100];
	for(c=0;c<=iX;c++)
	{
		for(j=0;j<=iY;j++)
		{
			if(arrayX[c]==arrayY[j])
			{arrayCommon[w]=arrayX[c];w++;}
		}
	}
	w=w-1;
	return arrayCommon[w];
} 

int main()
{
	int x,y;
	printf("Input intergers x y: \n\n");
	scanf("%d %d",&x,&y);
	printf("Their largest common factor is: %d\n",gcd(x,y));
	
}

