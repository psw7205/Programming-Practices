#include <bits/stdc++.h>

int main()
{
	int ar[100][100] = { 0 };

	for (int i = 0; i < 4; ++i)
	{
		int lbx, lby, rtx, rty;
		scanf("%d %d %d %d", &lbx, &lby, &rtx, &rty);

		int w = rtx - lbx;
		int h = rty - lby;

		for (int j = lbx; j < lbx + w; ++j)
		{
			for (int k = lby; k < lby + h; ++k)
			{
				ar[j][k] = 1;
			}
		}
	}
	
	int sum = 0;
	for (int i = 0; i < 100; ++i)
		for (int j = 0; j < 100; ++j)
			sum += ar[i][j];

	printf("%d", sum);

	return 0;
}