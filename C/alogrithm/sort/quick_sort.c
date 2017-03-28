#include <stdio.h>
int a[101], t;

void quick_sort(int left, int right)
{
	if(left > right)
		return;

	int i = left, j = right, pivot = a[left], temp;

	while(i != j)
	{
		while(a[j] >= pivot && i < j)
			j--;
		while(a[i] <= pivot && i < j)
			i++;

		if(i < j)
		{
			temp = a[i]; a[i] = a[j]; a[j] = temp;
		}
	}

	t = a[left]; a[left] = a[i]; a[i] = t;

	quick_sort(left, i-1);
	quick_sort(i+1, right);

}

int main(int argc, char const *argv[])
{
	int i,n;
	// 输入
	scanf("%d",&n);
	for(i = 0;i<n;i++)
		scanf("%d",&a[i]);
	// 调用以数组下标为准
	quick_sort(0,n-1);
	// 输出
	for(i=0;i<n;i++)
		printf("%d", a[i]);
	return 0;
}