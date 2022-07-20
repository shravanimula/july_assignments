/*
1
4  9
16 25 36
49 64 81 100
121 144 169 196 225
*/
#include<stdio.h>
int main()
{
	int i,j,rows,num=1;
	printf("enter the number of rows\n");
	scanf("%d",&rows);
	for(i=1;i<=rows;i++,printf("\n"))
	{
		for(j=1;j<=i;j++)
		{
			printf("%d ",num*num);
			num++;
		}
	}
}
