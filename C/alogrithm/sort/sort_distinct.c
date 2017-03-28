#include <stdio.h>

int temp,a[100];

void quick_sort(int left, int right)
{
	if(left > right)
		return;

	int i = left, j = right, pivot = a[left], t;
	while(i != j)
	{
		while(a[j] >= pivot && i < j)
			j--;
		while(a[i] <= pivot && i < j)
			i++;

		if(i < j)
		{
			t = a[i]; a[i] = a[j]; a[j] = t;
		}
	}
	
	temp = a[left]; a[left] = a[i]; a[i] = temp;

	quick_sort(left, i-1);
	quick_sort(i+1, right);
	
}

int main(int argc, char const *argv[])
{
	int i,n;
	scanf("%d",&n);
	for(i=0;i<n;i++)
		scanf("%d", &a[i]);

	quick_sort(0,n-1);

	printf("%d,", a[0]);
	for(i=1;i<n;i++)
		if(a[i]!=a[i-1])
			printf("%d,", a[i]);
	return 0;
}