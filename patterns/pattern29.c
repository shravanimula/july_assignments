/*
1
2 4
3 6 9
4 8 12 16
5 10 15 20 25
*/
#include<stdio.h>
int main()
{
	int i,j,rows,num=1;
	printf("enter the no.of rows\n");
	scanf("%d",&rows);
	for(i=1;i<=rows;i++,printf("\n"))
	{
		for(j=1;j<=i;j++)
		{
			printf("%d ",num*j);
		}
		num++;
	}
}
