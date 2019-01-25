#include <bits/stdc++.h>

using namespace std;

int main()
{
	int n;
	scanf("%d", &n);

	int ar[1001][5] = { 0 };
	int stu[1001] = { 0 };
	bool check[1001][1001] = { 0 };

	for (int i = 0; i < n; ++i)
		for (int j = 0; j < 5; ++j)
			scanf("%d", &ar[i][j]);

	for (int i = 0; i < 5; ++i)
	{
		for (int j = 0; j < n; ++j)
		{
			for (int k = 0; k < n; ++k)
			{
				if (j == k)
					continue;

				if (ar[j][i] == ar[k][i] && check[j][k] == false)
				{
					stu[j]++;
					check[j][k] = true;
				}
			}
		}
	}

	int max = -1, maxIdx = -1;
	for (int i = 0; i < n; ++i)
	{
		if (stu[i] > max)
		{
			max = stu[i];
			maxIdx = i + 1;
		}
	}

	printf("%d", maxIdx);

	return 0;
}
