#include <bits/stdc++.h>
using namespace std;

int ar[100000];

int gcd(int a, int b)
{
	if (a % b == 0)
		return b;

	return gcd(b, a % b);
}

int main()
{
	int n;
	scanf("%d", &n);

	int prev = 0;
	for (int i = 0; i < n; ++i)
	{
		int tmp;
		scanf("%d", &tmp);
		ar[i] = tmp - prev;
		prev = tmp;
	}

	int g = ar[1];
	for (int i = 1; i < n; ++i)
	{
		g = gcd(g, ar[i]);
	}

	int cnt = 0;
	for (int i = 1; i < n; ++i)
	{
		if (ar[i] == g)
			continue;

		cnt += (ar[i] / g - 1);
	}

	printf("%d", cnt);

	return 0;
}