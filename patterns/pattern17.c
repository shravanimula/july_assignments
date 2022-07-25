/*
e
d e
c d e
b c d e
a b c d e
*/
#include<stdio.h>
int main()
{
	int i,j,rows,ch=96;
	printf("enter the no.of rows\n");
	scanf("%d",&rows);
	for(i=rows;i>=1;i--,printf("\n"))
	{
		for(j=i;j<=rows;j++)
		{
			printf("%c ",ch+j);
		}
	}
}
