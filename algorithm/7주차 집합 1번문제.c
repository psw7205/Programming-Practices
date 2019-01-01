#include<stdio.h>
#include<stdlib.h>
#pragma warning(disable:4996)

typedef struct set
{
	int element;
	struct set * next;
}set;

set * getSet()
{
	set * new = (set*)malloc(sizeof(set));
	new->next = NULL;
	return new;
}

set * addSet(set * k, int ind)
{
	while (k->next != NULL)
		k = k->next;
	set *new = getSet();
	new->element = ind;
	new->next = NULL;
	k->next = new;
	return new;
}

void subSet(set *a, set *b)
{
	a = a->next;
	b = b->next;
	while (a != NULL && b != NULL)
	{
		if (a->element > b->element)
			b = b->next;
		else if (a->element == b->element)
		{
			a = a->next;
			b = b->next;
		}
		else

			break;
	}
	if (a == NULL)
		printf("0");
	else
		printf("%d", a->element);
}

int main()
{
	int n, m;
	set * a = getSet();
	set * b = getSet();
	scanf("%d", &n);
	for (int i = 0; i < n; i++)
	{
		scanf("%d", &m);
		addSet(a, m);
	}
	scanf("%d", &n);
	for (int i = 0; i < n; i++)
	{
		scanf("%d", &m);
		addSet(b, m);
	}
	subSet(a, b);
	return 0;
}