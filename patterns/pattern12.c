/*
a
b b
c c c
d d d d
e e e e e
*/
#include<stdio.h>
int main()
{
	int i,j,rows,ch=97;
	printf("enter the number of rows\n");
	scanf("%d",&rows);
	for(i=1;i<=rows;i++,printf("\n"))
	{
		for(j=1;j<=i;j++)
		{
			printf("%c ",ch);
		}
		ch++;
	}
}
