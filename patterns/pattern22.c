/*
1
3 5
7 9 11
13 15 17 19
21 23 25 27 29
*/
#include<stdio.h>
int main()
{
	int i,j,rows,num=0;
	printf("enter the no.of rows\n");
	scanf("%d",&rows);
	for(i=1;i<=rows;i++,printf("\n"))
	{
		for(j=1;j<=i;j++)
		{
			num++;
			printf("%d ",num);
			num=num+1;
		}
	}
}
