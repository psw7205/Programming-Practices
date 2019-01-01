#include <stdio.h>
#include <string.h>
#include <malloc.h>
#pragma warning(disable:4996)

typedef struct Node{
	struct Node* next;
	char data;
}Node;

Node* getNode()
{
	Node *a = (Node*)malloc(sizeof(Node));
	a->next = NULL;
	a->data = '\0';
	return a;
}

int isEmty(int cnt)
{
	if (cnt == 0)
		return 1;
	return 0;
}

Node* PUSH(Node* head, char c ,int* cnt)
{
	Node* newNode = getNode();
	Node* temp = head->next;
	newNode->data = c;

	head->next = newNode;
	newNode->next = temp;
	(*cnt)++;
	return newNode;
}

char POP(Node* head, int* cnt)
{
	if (isEmty(*cnt))
	{
		printf("empty\n");
		return 0;
	}
	char temp = head->next->data;
	Node* f = head->next;
	head->next = head->next->next;
	(*cnt)--;
	free(f);
	return temp;
}

int main()
{
	int cnt = 0;
	char a[10], c;
	Node* head = getNode();

	while (1) {
		scanf("%s", a);
		getchar();

		if (!strcmp(a, "PUSH"))
		{
			scanf("%c", &c);
			PUSH(head, c, &cnt);
		}

		if (!strcmp(a, "POP"))
		{
			c = POP(head, &cnt);
			if (c != 0)
				printf("%c\n", c);
		}
	}


	return 0;
}