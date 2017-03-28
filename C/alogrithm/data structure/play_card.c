#include <stdio.h>
struct player
{
	int queue[100];
	int head;
	int tail;
};
struct table
{
	int stack[100];
	int top;
};
int i;

void playcard(struct player* player, struct table* table)
{
	int t=player->queue[player->head];
	// printf("t=%d\n", t);
	int flag=0;//判断打出的拍桌面上是否已经存在：0不存在，1存在。
	for(i=0; i<table->top; i++)
	{
		if(t==table->stack[i]){flag=1; break;}
	}

	if(flag==0)
	{
		table->stack[table->top++]=t;
		player->head++;
	}

	else if(flag==1)
	{
		player->queue[player->tail++]=t;
		player->head++;
		while(table->stack[table->top-1]!=t)
		{
			player->queue[player->tail++]=table->stack[table->top-1];
			table->top--;
		}
		player->queue[player->tail++]=table->stack[table->top-1];
		table->top--;
	}
}

int main(int argc, char const *argv[])
{
	struct player a={{2,4,1,2,5,6},0,6}, b={{3,1,3,5,6,4},0,6};
	struct table s={.top=0};
	int book[10];
	for(i=1; i<10; i++)
		book[i]=0;

	while(a.head<a.tail && b.head<b.tail)
	{
		playcard(&a, &s);
		// printf("cards on a: ");
		// for(i=a.head; i<a.tail; i++)
		// 	printf("%d", a.queue[i]);
		// printf("\n");
		// printf("a play; a.head=%d, a.tail=%d, b.head=%d, b.tail=%d, s.top=%d\n",a.head, a.tail, b.head, a.tail, s.top);
		// printf("cards on table:");
		// for(i=0; i<s.top; i++)
		// 	printf("%d", s.stack[i]);
		// printf("\n");
		
		playcard(&b, &s);
		// printf("cards on b: ");
		// for(i=b.head; i<b.tail; i++)
		// 	printf("%d", b.queue[i]);
		// printf("\n");
		// printf("b play; a.head=%d, a.tail=%d, b.head=%d, b.tail=%d, s.top=%d\n",a.head, a.tail, b.head, a.tail, s.top);
		// printf("cards on table:");
		// for(i=0; i<s.top; i++)
		// 	printf("%d", s.stack[i]);
		// printf("\n\n");
	}


	if(b.head==b.tail)
	{
		printf("player a wins\n");
		printf("a's cards is ");
		// printf("a.head%d, a.tail%d, b.head%d, b.tail%d",a.head, a.tail, b.head, a.tail);
		for(i=a.head; i<a.tail; i++)
			printf("%d", a.queue[i]);
		if(s.top>-1)
		{
			printf("\nthe cards on table:");
			for(i=0; i<s.top; i++)
				printf("%d", s.stack[i]);
		}
		else
			printf("\nno cards on table");
	}
	else if(a.head==a.tail)
	{
		printf("player b wins\n");
		printf("b's cards is ");
		for(i=b.head; i<b.tail; i++)
			printf("%d", b.queue[i]);
		if(s.top>-1)
		{
			printf("\nthe cards on table:");
			for(i=0; i<s.top; i++)
				printf("%d", s.stack[i]);
		}
		else
			printf("\nno cards on table");
	}
	return 0;
}
