/*
 0
 -1 2
 -3 4 -5
 6 -7 8 -9
10 -11 12 -13 14
*/
#include<stdio.h>
int main()
{
	int i,j,rows,num=0;
	printf("enter the no.of rows\n");
	scanf("%d",&rows);
	for(i=1;i<=rows;i++,printf("\n"))
	{
		for(j=1;j<=i;j++)
		{
			if(num%2!=0)
				printf("-%d ",num);
			else printf("%d ",num);
			num++;
		}
	}
}
