#include<stdio.h>
#include<string.h>
#define SIZE 100
void mystr_len(char []);
void mystr_lenptr(char *);
int main()
{
	char str[SIZE];
	printf("enter the string:\n");
	scanf(" %[^\n]s",str);
	printf("length of the string:%ld\n",strlen(str));
	mystr_len(str);
	mystr_lenptr(str);
}
void mystr_len(char s[])
{
	int i,length=0;
	for(i=0;s[i]!='\0';i++)
	{
		length++;
	}
	printf("length of the given string:%d\n",length);
}
void mystr_lenptr(char *s)
{
	int i,len=0;
	for(i=0;*(s+i)!='\0';i++)
	{
		len++;
	}
	printf("length of the given string is:%d\n",len); }
