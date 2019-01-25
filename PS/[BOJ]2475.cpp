#include <bits/stdc++.h>
using namespace std;

int main()
{
	int ar[5];
	int result = 0;

	for (int i = 0; i < 5; ++i)
	{
		cin >> ar[i];
		ar[i] = ar[i] * ar[i];
		result += ar[i];
	}

	cout << result % 10;

	return 0;
}