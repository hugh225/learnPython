#include <stdio.h>
#include <stdlib.h>
struct node
{
	int data;
	struct node *next;
};

int main(int argc, char const *argv[])
{
	struct node *head, *now, *prev, *temp;
	int i, n, a;
	head=NULL;
//按序构建链表
	scanf("%d", &n);
	for(i = 0; i < n; i++)
	{
		scanf("%d", &a);
		now=(struct node *)malloc(sizeof(struct node));
		now->data=a;
		now->next=NULL;
		if(head==NULL)
			head=now;
		else
			prev->next=now;
		prev=now;
	}
//从头遍历链表
	temp=head;
	while(temp!=NULL)
	{
		printf("%d ", temp->data);
		temp=temp->next;
	}
	return 0;
}