/*
1
2 1
3 2 1
4 3 2 1
5 4 3 2 1
*/
#include<stdio.h>
int main()
{
	int rows,i,j;
	printf("enter the no.of rows:\n");
	scanf("%d",&rows);
	for(i=1;i<=rows;i++,printf("\n"))
	{
		for(j=i;j>=1;j--)
		{
			printf("%d ",j);
		}
	}
}

