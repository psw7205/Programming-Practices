#pragma warning(disable : 4996)
#include <bits/stdc++.h>
using namespace std;

int main()
{
	int n, m;
	cin >> n >> m;

	int min = std::min(n, m);

	int gcd = 1;
	for (int i = 2; i <= min; ++i)
	{
		if (n % i == 0 && m % i == 0)
		{
			gcd = std::max(gcd, i);
		}
	}

	cout << gcd << endl;
	cout << n * m / gcd << endl;

	return 0;
}