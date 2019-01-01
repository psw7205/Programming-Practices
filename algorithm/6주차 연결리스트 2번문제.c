#include<stdio.h>
#include <stdlib.h>
#pragma warning(disable:4996)

typedef struct poly {
	struct poly * next;
	int coef;
	int exp;
}poly;

poly * getPoly()
{
	poly * new = (poly*)malloc(sizeof(poly));
	new->next = NULL;
	return new;
}

poly * appendTerm(poly * k, int c, int e)
{
	while (k->next != NULL)
	{
		k = k->next;
	}
	poly * new = getPoly();
	new->coef = c;
	new->exp = e;
	k->next = new;

	return new;
}

poly * addPoly(poly * x, poly * y)
{
	poly * result = getPoly();

	x = x->next;
	y = y->next;

	int sum;

	while (x != NULL && y != NULL)
	{
		if (x->exp > y->exp)
		{
			appendTerm(result, x->coef, x->exp);
			x = x->next;
		}
		else if (x->exp < y->exp)
		{
			appendTerm(result, y->coef, y->exp);
			y = y->next;
		}
		else
		{
			sum = x->coef + y->coef;
			if (sum != 0)
				appendTerm(result, sum, x->exp);
			x = x->next;
			y = y->next;
		}
	}

	while (y != NULL)
	{
		appendTerm(result, y->coef, y->exp);
		y = y->next;
	}
	
	while (x != NULL)
	{
		appendTerm(result, x->coef, x->exp);
		x = x->next;
	}
	return result;
}

void printPoly(poly * a)
{
	a = a->next;
	while (a != NULL)
	{
		printf(" %d %d", a->coef, a->exp);
		a = a->next;
	}
}

int main()
{
	int c = 0, e = 0, n = 0;
	poly *a = getPoly();
	poly *b = getPoly();
	poly * sum = getPoly();

	scanf("%d", &n);

	for (int i = 0; i < n; i++)
	{
		scanf("%d %d", &c, &e);
		appendTerm(a, c, e);
	}

	scanf("%d", &n);

	for (int i = 0; i < n; i++)
	{
		scanf("%d %d", &c, &e);
		appendTerm(b, c, e);
	}

	printPoly(addPoly(a,b));

	return 0;
}