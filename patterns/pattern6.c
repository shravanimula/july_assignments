/*
5
5 4 
5 4 3
5 4 3 2
5 4 3 2 1
*/
#include<stdio.h>
int main()
{
	int i,j,rows;
	printf("enter the number of rows\n");
	scanf("%d",&rows);
	for(i=rows;i>=1;i--,printf("\n"))
	{
		for(j=rows;j>=i;j--)
		{
			printf("%d ",j);
		}
	}
}
