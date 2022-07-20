/*
5
4 5
3 4 5
2 3 4 5
1 2 3 4 5
*/
#include<stdio.h>
int main()
{
	int i,j,rows;
	printf("enter the number of rows\n");
	scanf("%d",&rows);
	for(i=rows;i>=1;i--,printf("\n"))
	{
		for(j=i;j<=rows;j++)
		{
			printf("%d ",j);
		}
	}
}
