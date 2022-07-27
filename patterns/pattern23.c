/*
0
2 4
6 8 10
12 14 16 18
20 22 24 26 28
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
			printf("%d ",num);
			num=num+2;
		}
	}
}
