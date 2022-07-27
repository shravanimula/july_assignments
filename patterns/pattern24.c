/*
a
A A
a a a
A A A A
a a a a a
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
			if(i%2!=0)
				printf("%c ",ch);
			else printf("%c ",ch-32);
		}
	}
}
