#include<stdio.h>
#define SIZE 100
void mystrcmp(char const [],char const []);
int main()
{
	char s1[SIZE],s2[SIZE];
	printf("enter a string1\n");
	scanf(" %[^\n]s",s1);
	printf("enter a string2\n");
	scanf(" %[^\n]s",s2);
	printf("s1=%s\ts2=%s\n",s1,s2);
	mystrcmp(s1,s2);
}
void mystrcmp(char const s1[],char const s2[])
{
	int i=0,j=0,flag;
	while(s1[i]!='\0' && s2[j]!='\0')
	{
		if(s1[i]==s2[j])
		{
			flag=0;
		}
		else
		{
			flag=1;
			break;
		}
		i++;
		j++;
	}
	if(flag==0)
		printf("strings are equal\n");
	else
		printf("strings are not equal\n");
}

			
