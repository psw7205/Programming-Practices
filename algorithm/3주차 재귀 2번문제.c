#include<stdio.h>
#pragma warning(disable: 4996)

int main()
{
	unsigned int a;

	scanf("%d", &a);

	func(a);

	return 0;

}

int func(int n)
{
	int result;

	if (n < 1)
		return 0;
	else
	{	
		func(n / 10);
		result = n % 10;
		printf("%d \n", result);
	}
}
