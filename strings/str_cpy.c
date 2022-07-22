#include<stdio.h>
#define SIZE 100
void mystrcpy(char [] ,const char []);
int main()
{
	char str1[SIZE],str2[SIZE];
	printf("enter string1\n");
	scanf(" %[^\n]s",str1);
	printf("enter the string2\n");
	scanf(" %[^\n]s",str2);
	printf("str1=%s\tstr2=%s\n",str1,str2);
	mystrcpy(str2,str1);
}
void mystrcpy(char dest[],const char src[])
{
	int i,j;
	for(i=0;src[i]!='\0';i++)
	{
		dest[i]=src[i];
	}
	dest[i]='\0';
	printf("destination of string:%s\n",dest);
	printf("source of string:%s\n",src);
}
