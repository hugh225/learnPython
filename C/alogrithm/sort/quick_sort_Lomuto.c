#include <stdio.h>

int a[101],n,count=0;

void q_sort(int left,int right)
{
	if(left > right)
		return;

	int pivotIndex = left;
	int storeIndex = pivotIndex + 1;
	int i,temp;
	for(i = pivotIndex + 1; i <= right; i++)
		if(a[i] < a[pivotIndex])
		{
			temp = a[i]; a[i] = a[storeIndex]; a[storeIndex] = temp;
			storeIndex++;
		}
	temp = a[pivotIndex]; a[pivotIndex] = a[storeIndex-1]; a[storeIndex-1] = temp;

	q_sort(left,storeIndex-2);
	q_sort(storeIndex,right);
}

int main(int argc, char const *argv[])
{
	int i,j;
	// 输入数组
	scanf("%d",&n);
	for(i = 0; i < n; i++)
		scanf("%d",&a[i]);
	// 调用函数
	q_sort(0, n-1);
	// 输出数组
	for (i = 0; i < n; i++)
	{
		printf("%d", a[i]);
	}
	return 0;
}