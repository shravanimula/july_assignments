/*
1
* *
2 2 2
* * * *
3 3 3 3 3
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
			if(i%2!=0)
				printf("%d ",num);
			else
				printf("* ");
		}
		if(i%2!=0)
			num++;
	}
}
