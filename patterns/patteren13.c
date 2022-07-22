/*
 e
 d d
 c c c
 b b b b
 a a a a a
 */
#include<stdio.h>
int main()
{
	int i,j,rows,ch=101;
	printf("enter number of rows\n");
	scanf("%d",&rows);
	for(i=1;i<=rows;i++,printf("\n"))
	{
		for(j=1;j<=i;j++)
		{
			printf("%c ",ch);
		}
		ch--;
	}
}
