#include <stdio.h>

int main(int argc, char const *argv[])
{
	int i,j=0,swapped,t,a[5]={5,3,4,1,2};
	do
	{
		swapped = 0;
		for(i = 0; i < 5-1-j; i++)
			if(a[i] < a[i+1])
			{
				t=a[i];a[i]=a[i+1];a[i+1]=t;
				swapped = 1;
			}
		j++;
	}
	while(swapped);

	for(i=0;i<5;i++)
	{
		printf("%d",a[i]);
	}
	return 0;
}