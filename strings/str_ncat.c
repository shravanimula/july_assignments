#include<stdio.h>
#define SIZE 100
void mystrncat(char [],const char[],int);
int main()
{
	char s1[SIZE],s2[SIZE];
	int n;
	printf("enter a string1\n");
	scanf(" %[^\n]s",s1);
	printf("enter a string2\n");
	scanf(" %[^\n]s",s2);
	printf("enter the no.of elements\n");
	scanf("%d",&n);
	printf("s1=%s\ts2=%s\n",s1,s2);
	mystrncat(s1,s2,n);
}
void mystrncat(char dest[],const char src[],int n)
{
	int i=0,j;
	while(dest[i]!='\0')
	{
		i++;
	}
	for(j=0;j<n && src[j]!='\0';j++)
	{
		dest[i++]=src[j];
	}
	dest[i]='\0';
	printf("destination string:%s\n",dest);
	printf("source string:%s\n",src);
}
