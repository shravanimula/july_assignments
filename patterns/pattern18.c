/*
a
b c
d e f
g h i j
k l m n o
*/
#include<stdio.h>
int main()
{
	int i,j,rows,ch=97;
	printf("enter the no.of rows\n");
	scanf("%d",&rows);
	for(i=1;i<=rows;i++,printf("\n"))
	{
		for(j=1;j<=i;j++)
		{
			printf("%c ",ch);
			ch++;
		}
	}
}
