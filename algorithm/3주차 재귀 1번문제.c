#include<stdio.h>
#pragma warning(disable: 4996)

int main()
{
	int a, result;

	scanf("%d", &a);
	
	result = add(a);
	
	printf("%d", result);

	return 0;

}

int add(int n)
{
	if (n <= 1)
		return 1;
	else
		return n + add(n-1);

}