/*
0
1 -1
2 -2 2
3 -3 3 -3
4 -4 4 -4 4
*/
#include<stdio.h>
int main()
{
	int i,j,rows;
	printf("enter the number of rows\n");
	scanf("%d",&rows);
	for(i=0;i<rows;i++,printf("\n"))
	{
		for(j=0;j<=i;j++)
		{
			if(j%2==0)
				printf("%d ",i);
			else
				printf("%d ",-i);
			
		}
	}
}
