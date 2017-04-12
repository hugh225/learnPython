#include <stdio.h>
#include <stdlib.h>
struct node
{
	int data;
	struct node *next; 
};
//从头开始一次填充链表
int main(int argc, char const *argv[])
{
	int n,i,a;
	struct node *head, *now, *prev, *temp;//此处head为链表头指针，now为当前节点指针，perv为前一个节点指针
	head=NULL;
	scanf("%d", &n);//输入链表个数
	for (i = 0; i < n; i++)
	{
		scanf("%d", &a);//输入数据
		now=(struct node *)malloc(sizeof(struct node));//将当前节点指针指向刚申请到的struct node地址
		now->data=a;
		now->next=NULL;
		if(head==NULL)
			head=now;
		else
			prev->next=now;
		prev=now;//当前指针变为前一节点指针，now腾出去指向新生成的node，成为新的当前node指针。
		
	}
//从头开始遍历链表
	temp=head;
	while(temp!=NULL)
	{
		printf("%d ", temp->data);
		temp=temp->next;
	}

		return 0;
}