#pragma warning(disable: 4996)
#include <stdio.h>


int main()
{

	int a = 0, b = 0;

	scanf("%d %d", &a, &b);


	printf("%d", modulo(a, b));

	return 0;
}

int modulo(int a, int b)
{

	for (; a >= b; )
		a = a - b;

	return a;
}
