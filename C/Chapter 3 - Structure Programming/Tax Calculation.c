#include "stdio.h"
int main()
{
	int ratio;
	float salary,tax;
	scanf("%f",&salary);
	switch(ratio=salary/250)
	{
	case 0:
	case 1:
	case 2: tax=salary*0.01; printf("tax=%10.2fRMB\n",tax); break;
	case 3:
	case 4:
	case 5:
	case 6:
	case 7:
	case 8: tax=7.5+(salary-750)*0.02; printf("tax=%10.2fRMB\n",tax); break;
	case 9:
	case 10:
	case 11:
	case 12:
	case 13:
	case 14: tax=37.5+(salary-2250)*0.03; printf("tax=%10.2fRMB\n",tax); break;
	case 15:
	case 16:
	case 17:
	case 18:
	case 19:
	case 20: tax=82.5+(salary-3750)*0.04; printf("tax=%10.2fRMB\n",tax); break;
	case 21:
	case 22:
	case 23:
	case 24:
	case 25:
	case 26:
	case 27: tax=142.5+(salary-5250)*0.05; printf("tax=%10.2fRMB\n",tax); break;
	default: tax=230.0+(salary-7000)*0.06; printf("tax=%10.2fRMB\n",tax); break;
	}
	return 0;
	
} 