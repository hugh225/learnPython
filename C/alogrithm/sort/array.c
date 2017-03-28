#include <stdio.h>

int main(int argc, char const *argv[])
{
	// 初始化数组(100个0)
	int book[101],i,j,t,n;
	for(i = 0; i < 101; i++)
		book[i] = 0;
	// 接收输入数据（先输入个数，再输入数值）
	scanf("%d",&n);
	for(i = 0; i < n; i++)
	{
		scanf("%d",&t);
		book[t]++;
	}
	// 输出结果
	for (i = 0; i < 101; i++)
		for (j = 0; j < book[i]; j++)
			printf("%d,",i);

	return 0;
}