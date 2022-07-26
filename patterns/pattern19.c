/*
1
0 1
0 1 0
1 0 1 0
1 0 1 0 1
*/
#include<stdio.h>
int main()
{
	int i,j,rows,num=0;
	printf("enter a no.of rows\n");
	scanf("%d",&rows);
	for(i=1;i<=rows;i++,printf("\n"))
	{
		for(j=1;j<=i;j++)
		{
			num++;
			printf("%d ",num%2);
		}
	}
}
