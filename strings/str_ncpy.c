#include<stdio.h>
#define SIZE 100
void mystr_ncpy(char [],const char [],int);
int main()
{
	char s1[SIZE],s2[SIZE];
	int n,len;
	printf("enter a string1\n");
	scanf(" %[^\n]s",s1);
	printf("enter a string2\n");
	scanf(" %[^\n]s",s2);
	printf("enter the no.of elments wants to copy\n");
	scanf("%d",&n);
	printf("s1=%s\ts2=%s\n",s1,s2);
	mystr_ncpy(s2,s1,n);
}
void mystr_ncpy(char dest[],const char src[],int n)
{
	int i;
	for(i=0;i<n && src[i]!='\0';i++)
	{
		dest[i]=src[i];
	}
	dest[i]='\0';
	printf("Destination string:%s\n",dest);
	printf("source string:%s\n",src);
}
