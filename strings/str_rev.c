#include<stdio.h>
#define SIZE 100
int mystrlen(char []);
void strrev(char [],int );
int main()
{
	char s1[SIZE];
	int len;
	printf("enter a string:\n");
	scanf(" %[^\n]s",s1);
	printf("before string reverse:%s\n",s1);
	len=mystrlen(s1);
	printf("length of string:%d\n",len);
	strrev(s1,len);
}
int mystrlen(char s[])
{
	int i,length=0;
	for(i=0;s[i]!='\0';i++)
	{
		length++;
	}
	return length;
}
void strrev(char s[],int n)
{
	int i,temp,j;
	for(i=0,j=n-1;i<j;i++,j--)
	{
		temp=s[i];
		s[i]=s[j];
		s[j]=temp;
	}
	printf("after reverse of string:%s\n",s);
}
