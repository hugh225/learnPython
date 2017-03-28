#include <stdio.h>
#include <string.h>
int main(int argc, char const *argv[])
{
	char a[100], s[100];
	int len, mid, i, top, next;
	
	gets(a);
	len = strlen(a);
	mid = len/2-1;
	top=0;	
	for(i=0; i<=mid; i++)
	{
		s[top++]=a[i];
	}
	top--;
	if(len%2==0)
		next=mid+1;
	else
		next=mid+2;

	for(i=next; i<len; i++)
	{
		if(s[top]!=a[i])
			break;
		top--;
	}
	
	if(top==-1)
		printf("yes!");
	else
		printf("no!");

	return 0;
}


