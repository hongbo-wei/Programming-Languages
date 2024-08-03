#include<stdio.h>
int main(void)
{
	int i,j,s=1;
	
	for(i=2;i<=200;i++){          //i=2
	    s=1;                       //reset value of s after every circulation
		for(j=2;j<=i/2;j++)
		{if(i%j==0)             //change / to %,  add {
				s=s+j;}                //add }
			if(s==i){
				printf("%d=1",i);
				for(j=2;j<=i/2;j++)
					if(i%j==0)	printf("+%d",j);  //change / to %
				printf("\n");
		        	} 
	 	
	                	}
		return 0;
	}
