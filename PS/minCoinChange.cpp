#include <bits/stdc++.h>	

using namespace std;

#define INF 1234567890

int length;
int values[100];
int coins[100];

int minCoin1(int x)
{
	if (x == 0)
		return 0;
	if (x < 0)
		return INF;

	int best = INF;
	for (auto coin : coins)
	{
		if (coin == 0)
			break;
		best = min(best, minCoin1(x - coin) + 1);
	}

	return best;
}

int minCoin2(int x)
{
	if (x == 0)
		return 0;
	if (x < 0)
		return INF;

	int best = INF;
	if (values[x])
		return values[x];

	for (auto coin : coins)
	{
		if (coin == 0)
			break;
		best = min(best, minCoin2(x - coin) + 1);
	}

	values[x] = best;
	return best;
}

int minCoin3(int x)
{
	values[0] = 0;
	for (int x = 1; x <= length; ++x)
	{
		values[x] = INF;
		for (auto coin : coins)
		{
			if (coin == 0)
				break;
			values[x] = min(values[x], values[x - coin] + 1);
		}
	}

	return values[x];
}


int main()
{
	
	cin >> length;

	for (int i = 0; i < length; i++)
	{
		cin >> coins[i];
	}

	int result;
	cin >> result;

	cout << minCoin1(result) << endl;
	cout << minCoin2(result) << endl;
	cout << minCoin3(result) << endl;
	
	return 0;
}