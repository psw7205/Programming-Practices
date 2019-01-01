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

void print(set *a)
{
	a = a->next;
	while (a != NULL)
	{
		printf(" %d", a->element);
		a = a->next;
	}
	printf("\n");
}

set * unionSet(set * a, set * b)
{
	set * new = getSet();
	a = a->next;
	b = b->next;

	if (a == NULL && b == NULL)
	{
		addSet(new, 0);
		return new;
	}

	while (a != NULL || b != NULL)
	{
		if (a == NULL)
		{
			addSet(new, b->element);
			b = b->next;
		}
		else if (b == NULL)
		{
			addSet(new, a->element);
			a = a->next;
		}
		else if (a->element > b->element)
		{
			addSet(new, b->element);
			b = b->next;
		}
		else if (a->element < b->element)
		{
			addSet(new, a->element);
			a = a->next;
		}
		else
		{
			addSet(new, a->element);
			a = a->next;
			b = b->next;
		}
	}
	return new;
}

set * intersectSet(set *a, set *b)
{
	set * new = getSet();
	a = a->next;
	b = b->next;

	if (a == NULL || b->next == NULL)
	{
		addSet(new, 0);
		return new;
	}

	while (a != NULL && b != NULL)
	{
		if (a->element > b->element)
			b = b->next;
		else if (a->element < b->element)
			a = a->next;
		else
		{
			addSet(new, a->element);
			a = a->next;
			b = b->next;
		}
	}

	return new;
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

	print(unionSet(a, b));
	print(intersectSet(a, b));

	return 0;
}