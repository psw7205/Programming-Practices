#include <stdio.h>
#include <stdlib.h>
#pragma warning(disable:4996)

typedef struct node {
	struct node *llink;
	char data;
	struct node *rlink;
}node;

node *head;
node *tail;

node * getnode()
{
	node * DL = (node*)malloc(sizeof(node));
	return DL;
}

void initList()
{
	head = getnode();
	tail = getnode();

	head->rlink = tail;
	tail->llink = head;

	return;
}

node * Curser(int index)
{
	node *Cur = head;
	for (int i = 0; i < index; i++)
	{
		Cur = Cur->rlink;
		if (Cur == tail)
		{
			printf("invalid position\n");
			Cur = NULL;
			return Cur;
		}
	}
	return Cur;
}


void printList()
{
	node *DL = head->rlink;
	while (DL != tail)
	{
		printf("%c", DL->data);
		DL = DL->rlink;
	}
	printf("\n");
	return;
}

node * Add(int index, char c)
{
	node *New = getnode();
	node *Cur = Curser(index);
	if (Cur == NULL)
	{
		return Cur;
	}
	New->data = c;
	New->llink = Cur;
	New->rlink = Cur->rlink;
	Cur->rlink->llink = New;
	Cur->rlink = New;

	return New;
}

node* del(int index)
{
	node * Cur = Curser(index);
	if (Cur == NULL)
	{
		return '\0';
	}

	Cur->rlink->llink = Cur->llink;
	Cur->llink->rlink = Cur->rlink;
	free(Cur);
}


int main()
{
	initList();
	node * temp;

	int n, pos;
	char a, c;

	scanf("%d", &n);

	for (int i = 0; i < n; i++)
	{
		scanf(" %c", &a);

		if (a == 'A')
		{
			scanf("%d %c", &pos, &c);
			Add(pos - 1, c);
		}
		else if (a == 'D')
		{
			scanf("%d", &pos);
			del(pos);
		}
		else if (a == 'G')
		{
			scanf("%d", &pos);
			temp = Curser(pos);
			if (temp != NULL)
				printf("%c\n", temp->data);
		}
		else if (a == 'P')
		{
			printList();
		}
		else
		{
			break;
		}
	}

	return 0;
}