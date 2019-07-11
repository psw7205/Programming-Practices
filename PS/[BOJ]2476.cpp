#include <bits/stdc++.h>
using namespace std;

int main()
{
	int n;

	scanf("%d", &n);

	int maxPrize = 0;
	for (int i = 0; i < n; ++i)
	{
		int a, b, c, flag, dice = 0;

		scanf("%d %d %d", &a, &b, &c);

		if (a == b)
		{
			dice++;
			flag = a;
		}

		if (a == c)
		{
			dice++;
			flag = a;
		}

		if (b == c)
		{
			dice++;
			flag = b;
		}

		int prize = 0;
		switch (dice)
		{
		case 0:
			prize = (a > b ? a > c ? a : c : b > c ? b : c) * 100;
			break;
		case 1:
			prize = 1000 + flag * 100;
			break;

		case 3:
			prize = 10000 + flag * 1000;
			break;

		default:
			break;
		}

		if (maxPrize < prize)
			maxPrize = prize;
	}

	printf("%d", maxPrize);

	return 0;
}