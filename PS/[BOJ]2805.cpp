#include <bits/stdc++.h>
using namespace std;

long long bigTree = -1;

void search(vector<long long> vec, long long small ,long long big, long long key)
{
	long long maxH = (big - small)/2 + small;
	if (small > big)
	{
		printf("%lld", big);
		return;
	}

	long long sum = 0;

	for (long long i : vec)
	{
		if (i > maxH)
			sum += i - maxH;
	}

	if (sum > key)
	{
		search(vec, maxH + 1, big, key);
	}
	else if (sum < key)
	{
		search(vec, small, maxH - 1 , key);
	}
	else
	{
		printf("%lld", maxH);
	}

}

int main()
{
	long long n, m;

	scanf("%lld %lld", &n, &m);
	vector<long long> vec;
	for (long long i = 0; i < n; ++i)
	{
		long long tmp;
		scanf("%lld", &tmp);
		vec.push_back(tmp);
	}

	for (long long i : vec)
	{
		bigTree = std::max(i, bigTree);
	}

	search(vec, 1, bigTree, m);

	return 0;
}