#include <bits/stdc++.h>
using namespace std;

int main()
{
	int n, cnt = 0;
	scanf("%d", &n);
	for (int i = 0; i < n; ++i)
	{
		int prime;
		scanf("%d", &prime);

		int j;
		for (j = 2; j < prime; ++j)
		{
			if (prime % j == 0)
				break;
		}

		if (j == prime)
			cnt++;
	}

	printf("%d", cnt);

	return 0;
}