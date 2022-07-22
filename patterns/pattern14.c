/*
a
a b
a b c
a b c d
a b c d e
*/
#include<stdio.h>
int main()
{
	int i,j,rows,ch=96;
	printf("enter no.of rows\n");
	scanf("%d",&rows);
	for(i=1;i<=rows;i++,printf("\n"))
	{
		for(j=1;j<=i;j++)
		{
			printf("%c ",ch+j);
		}
	}
}

