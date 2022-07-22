#include<stdio.h>
#define SIZE 100
void mystrcat(char [],const char []);
int main()
{
	char s1[SIZE],s2[SIZE];
	printf("enter a string1\n");
	scanf(" %[^\n]s",s1);
	printf("enter a string2\n");
	scanf(" %[^\n]s",s2);
	printf("s1=%s\ts2=%s\n",s1,s2);
	mystrcat(s1,s2);
}
void mystrcat(char dest[],const char src[])
{
	int i,j=0;
	while(dest[j]!='\0')
	{
		j++;
	}
	for(i=0;src[i]!='\0';i++)
	{
		dest[j++]=src[i];
	}
	dest[j]='\0';
	printf("destination string:%s\n",dest);
	printf("source string:%s\n",src);
}
