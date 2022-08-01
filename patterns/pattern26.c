/*
a
2 2
c c c
4 4 4 4
e e e e e
*/
#include<stdio.h>
int main()
{
	int i,j,rows;
	printf("enter the no.of rows\n");
	scanf("%d",&rows);
	for(i=1;i<=rows;i++,printf("\n"))
	{
		for(j=1;j<=i;j++)
		{
			if(i%2!=0)
				printf("%c ",i+96);
			else printf("%d ",i);
		}
	}
}
