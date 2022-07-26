/*
1
0 1
1 0 1
0 1 0 1
1 0 1 0 1
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
			{
				if(j%2!=0)
					printf("1 ");
				else printf("0 ");
			}
			else
			{
				if(j%2!=0)
					printf("0 ");
				else printf("1 ");
			}
		}
	}
}
