#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int main()
{
	int num;
	scanf("%d", &num);

	for (int i = 0; i < num; ++i)
	{

		int n, m;
		scanf("%d %d", &n, &m);

		ll dist = m - n;

		ll cnt = 1;
		ll max = 0;
		while (dist > max)
		{
			ll mid = (cnt + 1) / 2;

			if (cnt % 2 == 0)
			{
				max = mid * (mid + 1);
			}
			else
			{
				max = mid * mid;
			}

			cnt++;
		}

		printf("%lld\n", cnt - 1);
	}

	return 0;
}