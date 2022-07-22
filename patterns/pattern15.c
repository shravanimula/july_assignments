/*
a
b a
c b a
d c b a
e d c b a
*/
#include<stdio.h>
int main()
{
	int i,j,rows,ch=96;
	printf("enter the number of rows\n");
	scanf("%d",&rows);
	for(i=1;i<=rows;i++,printf("\n"))
	{
		for(j=i;j>=1;j--)
		{
			printf("%c ",ch+j);
		}
	}
}
