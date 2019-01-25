#include <bits/stdc++.h>
using namespace std;

int main()
{
	int day;
	cin >> day;

	int ar[5];

	for (int i = 0; i < 5; ++i)
		cin >> ar[i];

	int cnt = 0;
	for (int i = 0; i < 5; ++i)
	{
		if (ar[i] == day)
			cnt++;
	}

	cout << cnt;

	return 0;
}