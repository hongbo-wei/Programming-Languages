#include"stdio.h"
void print(int n)
{
	int g1,g2,s1,s2,b1,b2,q1,q2,h1,h2,sum; //nΪ�������֣�g,s,b,qΪ��ʮ��ǧ,h1,h2Ϊ���������� 
    g1=n%10;
	s1=(n%100)/10;
	b1=(n%1000)/100;
	q1=(n%10000)/1000;
	
	g2=(g1+9)%10;
	s2=(s1+9)%10;
	b2=(b1+9)%10;
	q2=(q1+9)%10;
	
	h1=q2;
	q2=s2;
	s2=h1;                      //ǧʮ��
	h2=b2;
	b2=g2;
	g2=h2;                       //�ٸ��� 
	
	sum=q2*1000+b2*100+s2*10+g2;
	
	printf("secretNumber is %d\n",sum);
}

int main()
{
	print(1257);
}

