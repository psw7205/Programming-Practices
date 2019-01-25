#include <bits/stdc++.h>

typedef struct {
	int s, b;
	int num[3];
}info;



int main()
{
	int n;
	scanf("%d", &n);
	info ar[100];

	for (int i = 0; i < n; ++i)
	{
		char num[3];
		int s, b;

		scanf(" %c%c%c %d %d", &num[0], &num[1], &num[2], &s, &b);

		ar[i].num[0] = num[0] - '0';
		ar[i].num[1] = num[1] - '0';
		ar[i].num[2] = num[2] - '0';
		ar[i].s = s;
		ar[i].b = b;
	}

	int cnt = 0;

	for (int i = 1; i <= 9; ++i)
	{
		for (int j = 1; j <= 9; ++j)
		{
			if (i == j)
				continue;
			for (int k = 1; k <= 9; ++k)
			{
				if (i == k || j == k)
					continue;

				int check = 0;
				for (int idx = 0; idx < n; ++idx)
				{
					int s = 0;
					int b = 0;

					if (ar[idx].num[0] == i)	
						s++;

					if (ar[idx].num[1] == j)
						s++;

					if (ar[idx].num[2] == k)
						s++;

					if (ar[idx].num[0] == j)
						b++;

					if (ar[idx].num[0] == k)
						b++;

					if (ar[idx].num[1] == i)
						b++;

					if (ar[idx].num[1] == k)
						b++;

					if (ar[idx].num[2] == i)
						b++;

					if (ar[idx].num[2] == j)
						b++;

					if (ar[idx].s == s && ar[idx].b == b)
						check++;
				}

				if (check == n)
					cnt++;
			}
		}
	}

	printf("%d", cnt);

	return 0;
}