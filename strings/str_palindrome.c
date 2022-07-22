#include<stdio.h>
#define SIZE 100
int mystr_len(char []);
void str_palindrome(char [],int);
void str_palindrome_ptr(char *,int);
int main()
{
	char str[SIZE];
	int len;
	printf("enter the string:\n");
	scanf(" %[^\n]s",str);
	len=mystr_len(str);
	printf("length of the string:%d\n",len);
	str_palindrome(str,len);
	str_palindrome_ptr(str,len);
}
int mystr_len(char s[])
{
	int i,length=0;
	for(i=0;s[i]!='\0';i++)
	{
		length++;
	}
	return length;
}
void str_palindrome(char s[],int n)
{
	int i,flag;
	for(i=0;i<n/2;i++)
	{
		if(s[i]==s[n-i-1])
		{
			flag=0;
		}
		else
		{
			flag=1;
			break;
		}
	}
	if(flag==0)
		printf("given string is palindrome:%s\n",s);
	else
		printf("given strings are not palindrome:%s\n",s);
}
void str_palindrome_ptr(char *st,int n)
{
	int i,flag;
	for(i=0;i<n/2;i++)
	{
		if((*(st+i))==(*(st+n-i-1)))
		{
			flag=0;
		}
		else
		{
			flag=1;
			break;
		}
	}
	if(flag==0)
		printf("given string  is palindrome:%s\n",st);
	else
		printf("given string is not a palindrome:%s\n",st);
}

