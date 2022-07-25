/*
e
e d
e d c
e d c b
e d c b a
*/
#include<stdio.h>
int main()
{
	int i,j,rows,ch=96;
	printf("enter the no.of rows\n");
	scanf("%d",&rows);
	for(i=rows;i>=1;i--,printf("\n"))
	{
		for(j=rows;j>=i;j--)
		{
			printf("%c ",ch+j);
		}
	}
}
