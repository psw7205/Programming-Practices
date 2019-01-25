#include <bits/stdc++.h>
using namespace std;

int main()
{
	int n, wantedIdx; 
	scanf("%d %d", &n, &wantedIdx);
	
	long long max = (long long)n * n;
	long long min = 1;
	long long result;

	while (true)
	{
		if (min > max)
		{
			break;
		}

		long long cnt = 0;
		long long mid = (max + min)/2;
		for (int i = 1; i <= n; ++i)
		{
			long long tmp = mid / i;

			if (tmp > n)
				tmp = n;

			cnt += tmp;
		}

		if (cnt >= wantedIdx)
		{
			result = mid;
			max = mid - 1;
		}
		else if (cnt < wantedIdx)
		{
			min = mid + 1;
		}
	}

	printf("%lld", result);

	return 0;
}