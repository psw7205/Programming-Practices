#include <bits/stdc++.h>
using namespace std;

int main()
{
	int ar[9][9] = {0};

	for (int i = 0; i < 9; ++i)
		for (int j = 0; j < 9; ++j)
			cin >> ar[i][j];

	int max = 0, row, col;
	for (int i = 0; i < 9; ++i)
	{
		for (int j = 0; j < 9; ++j)
		{
			if (max < ar[i][j])
			{
				max = ar[i][j];
				row = i;
				col = j;
			}
		}
	}

	cout << max << endl
		 << row + 1 << " " << col + 1;

	return 0;
}