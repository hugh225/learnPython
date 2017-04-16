#include <stdio.h>
#include <stdlib.h>

struct node
{
	int data;
	struct node *next;
};

int main(int argc, char const *argv[])
{
	int i,n,a;
	struct node *now, *prev, *head=NULL, *temp;
// 构建链表
	scanf("%d", &n);
	for(i=0; i<n; i++)
	{
		now=(struct node*)malloc(sizeof(struct node));
		scanf("%d", &a);
		now->data=a;
		now->next=NULL;
		if(head==NULL)
			head=now;
		else
			prev->next=now;
		prev=now;
	}
// 从头开始遍历链表
	temp=head;
	while(temp!=NULL)
	{
		printf("%d ", temp->data);
		temp=temp->next;
	}
	return 0;
}