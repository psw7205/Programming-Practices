#include <bits/stdc++.h>

using namespace std;
bool check[5][5];

int count()
{
	int cnt = 0;
	for (int i = 0; i < 5; ++i)
	{
		bool rowCheck = true;
		bool colCheck = true;
		for (int j = 0; j < 5; ++j)
		{
			rowCheck = rowCheck && check[i][j];
			colCheck = colCheck && check[j][i];
		}

		if (colCheck == true)
			cnt++;

		if (rowCheck == true)
			cnt++;
	}

	bool ltDiagonal = true;
	bool rtDiagonal = true;
	for (int i = 0; i < 5; ++i)
	{
		ltDiagonal = ltDiagonal && check[i][i];
		rtDiagonal = rtDiagonal && check[i][4 - i];
	}

	if (ltDiagonal == true)
		cnt++;

	if (rtDiagonal == true)
		cnt++;

	return cnt;
}

int main()
{
	int map[5][5];

	for (int i = 0; i < 5; ++i)
		for (int j = 0; j < 5; ++j)
			scanf("%d", &map[i][j]);

	int cnt = 0;
	while (cnt <= 25)
	{
		int tmp;
		scanf("%d", &tmp);

		for (int i = 0; i < 5; ++i)
		{
			for (int j = 0; j < 5; ++j)
			{
				if (map[i][j] == tmp)
				{
					check[i][j] = true;
					cnt++;
					int ret = count();
					if (ret >= 3)
					{
						printf("%d", cnt);
						return 0;
					}
				}
			}
		}
	}

	return 0;
}
