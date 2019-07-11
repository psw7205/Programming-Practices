#include <bits/stdc++.h>
using namespace std;

int ar[100];

int main()
{
	int n;
	scanf("%d", &n);

	for (int i = 0; i < n; ++i)
		scanf("%d", &ar[i]);

	int tmp = 0;
	int result = 0;
	for (int i = 1; i <= n; ++i)
	{
		result = ar[i - 1] * i - tmp;
		tmp += result;
		printf("%d ", result);
	}

	return 0;
}