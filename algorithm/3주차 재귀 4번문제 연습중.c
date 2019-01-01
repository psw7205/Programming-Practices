#include<stdio.h>
#pragma warning(disable: 4996)

int max(int arry[], int n)
{

	max(arry, n);

	if (n < 0)
	{
		return arry[0];
	}
	else
	{
		if (arry[n] > arry[n - 1])
			return arry[n];
		else
			return arry[n-1];

	}
	n = n - 1;
}

int main()
{
	int n, a = 0;
	int arry[21];

	scanf("%d", &n);

	for (int i = 0; i < n; i++)
		scanf("%d", &arry[i]);

	n--;

	a = max(arry, n);

	printf("%d", a);


	return 0;
}

