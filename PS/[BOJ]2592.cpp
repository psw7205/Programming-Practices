#include <bits/stdc++.h>

using namespace std;

bool compare(const pair<int, int> &a, const pair<int, int> &b)
{
	if (a.first == b.first)
		return a.second < b.second;

	return a.first > b.first;
}

int main()
{
	int sum = 0;
	int n[10];
	for (int i = 0; i < 10; ++i)
	{
		scanf("%d", &n[i]);
		sum += n[i];
	}
	sum /= 10;

	vector<pair<int, int>> min;
	min.resize(10);
	for (int i = 0; i < 10; ++i)
	{
		min[i].first = 0;
		min[i].second = n[i];

		for (int j = 0; j < 10; ++j)
		{
			if (i == j)
				continue;

			if (n[i] == n[j])
			{
				min[i].first++;
			}
		}
	}

	sort(min.begin(), min.end(), compare);

	printf("%d\n%d", sum, min[0].second);

	return 0;
}
