/*
1
b b
3 3 3
d d d d
5 5 5 5 5
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
				printf("%d ",i);
			else printf("%c ",i+96);
		}
	}
}
