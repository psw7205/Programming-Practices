#include <bits/stdc++.h>

using namespace std;

int main()
{
	int n;
	scanf("%d", &n);

	int ar[101][101] = {0};

	for (int i = 1; i <= n; ++i)
	{
		int x, y, w, h;
		scanf("%d %d %d %d", &x, &y, &w, &h);
		for (int j = x; j < x + w; ++j)
			for (int k = y; k < y + h; ++k)
				ar[j][k] = i;
	}

	for (int i = 1; i <= n; ++i)
	{
		int cnt = 0;
		for (int j = 0; j < 101; ++j)
		{
			for (int k = 0; k < 101; ++k)
			{
				if (ar[j][k] == i)
					cnt++;
			}
		}

		printf("%d\n", cnt);
	}

	return 0;
}
