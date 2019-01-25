#include <bits/stdc++.h>

int num[1001][1001] = { 0 };

void fill(int n, int m, int x, int y, int*cnt, int max)
{
	int i, j, k;
	if (*cnt > max) // 다 채우면 끝
		return;
	for (i = x; i < x + m; i++)
		num[y][i] = (*cnt)++; // 오른쪽 방향으로 채움
	if (y + 1 < n + y)
	{
		for (j = y + 1; j < n + y; j++) // 아랫방향으로 채움
			num[j][i - 1] = (*cnt)++;
		if (i - 2 >= x) // 왼쪽으로 이동가능하다면 
		{
			for (k = i - 2; k >= x; k--)
				num[j - 1][k] = (*cnt)++; // 왼쪽을 채우고
			for (i = j - 2; i > y; i--)
				num[i][k + 1] = (*cnt)++; // 위로 채운다
			fill(n - 2, m - 2, k + 2, i + 1, cnt, max); // 재귀하며 반복
		}
	}
}

int main()
{

	int n, m, k;
	scanf("%d %d %d", &n, &m, &k);

	if (k > n * m)
		printf("0");
	else {

		int cnt = 1;
		fill(n, m, 0, 0, &cnt, n*m);

		bool flag = false;
		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < m; j++)
			{
				if (k == num[i][j] && flag == false)
				{
					printf("%d %d", i + 1, j + 1);
					flag = true;
					break;
				}
			}

			if (flag == true)
				break;
		}
	}


	return 0;
}