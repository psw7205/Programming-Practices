#include <bits/stdc++.h>
using namespace std;

int main()
{
	int a[10], b[10], result = 0;

	for (int i = 0; i < 10; ++i)
	{
		scanf("%d", &a[i]);
	}

	for (int i = 0; i < 10; ++i)
	{
		scanf("%d", &b[i]);
	}

	for (int i = 0; i < 10; ++i)
	{
		if (a[i] != b[i])
			result += a[i] > b[i] ? 1 : -1;
	}

	if (result > 0)
		printf("A");
	else if (result < 0)
		printf("B");
	else
		printf("D");

	return 0;
}