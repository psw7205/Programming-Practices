#include <bits/stdc++.h>
using namespace std;

bool compare(const int a, const int b)
{
	if (abs(a) > abs(b))
		return true;

	return false;
}

int main()
{
	vector<int> vec;
	int n;
	scanf("%d", &n);

	for (int i = 0; i < n; ++i)
	{
		int tmp;
		scanf("%d", &tmp);
		vec.push_back(tmp);
	}

	sort(vec.begin(), vec.end(), compare);

	int min = numeric_limits<int>::max();
	int a, b;
	for (int i = 0; i < n - 1; ++i)
	{
		if (min > abs(vec[i] + vec[i + 1]))
		{
			min = abs(vec[i] + vec[i + 1]);
			a = i, b = i + 1;
		}
		else if (min == abs(vec[i] + vec[i + 1]))
		{
			a = std::min(vec[a], vec[b]) < std::min(vec[i], vec[i + 1]) ? a : i;
			b = a + 1;
		}
	}

	int big = vec[a] > vec[b] ? vec[a] : vec[b];
	int small = vec[a] < vec[b] ? vec[a] : vec[b];
	printf("%d %d", small, big);

	return 0;
}