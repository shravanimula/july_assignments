#include<stdio.h>
int main()
{
	int i,j,rows;
	printf("enter the number of rows\n");
	scanf("%d",&rows);
	for(i=1;i<=rows;i++,printf("\n"))
	{
		for(j=1;j<=i;j++)
		{
			if(j==1 || j==i)
				printf("* ");
			else if(i==rows)
				printf("* ");
			else
				printf("  ");
		}
	}
}
