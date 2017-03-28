#include <stdio.h>
int b[20],i;

struct queue
{
	int a[20];
	int head;
	int tail;
};

void decrypt()
{
	int i=0;
	while(q.head < q.tail)
	{
		b[i++]=q.a[q.head++];
		q.a[q.tail++]=q.a[q.head++];
	}
}

int main(int argc, char const *argv[])
{
	struct queue q={{6,3,1,7,5,8,9,2,4},0,9};
	decrypt();
	for(i=0; i<9; i++)
		printf("%d", b[i]);
	return 0;
}