#include <bits/stdc++.h>
using namespace std;

int s[1000][1000];
int ar[1000];

int main()
{
	int n;
	scanf("%d", &n);

	for (int i = 0; i < n; ++i)
		for (int j = 0; j < n; ++j)
			scanf("%d", &s[i][j]);

	int idx = 0;
	ar[0] = (s[0][1] + s[0][2] - s[1][2]) / 2;
	for (int i = 1; i < n; ++i)
	{
		ar[i] = s[0][i] - ar[0];
	}

	for (int i = 0; i < n; ++i)
		printf("%d ", ar[i]);

	return 0;
}