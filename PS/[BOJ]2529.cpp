#include <bits/stdc++.h>
using namespace std;

int k;
vector<int> vMax, vMin;
string str;

bool isPossible(vector<int> &num)
{
	for (int i = 0; i < str.length(); ++i)
	{
		if (str[i] == '>' && num[i] < num[i + 1])
			return false;

		else if (str[i] == '<' && num[i] > num[i + 1])
			return false;
	}

	return true;
}

int main()
{
	scanf("%d", &k);

	for (int i = 0; i < k; ++i)
	{
		char tmp;
		scanf(" %c", &tmp);
		str.push_back(tmp);
	}

	for (int i = 0; i < k + 1; ++i)
		vMin.push_back(i), vMax.push_back(9 - i);

	while (true)
	{
		if (isPossible(vMin))
			break;
		next_permutation(vMin.begin(), vMin.end());
	}

	while (true)
	{
		if (isPossible(vMax))
			break;
		prev_permutation(vMax.begin(), vMax.end());
	}

	for (int i = 0; i <= k; ++i)
		printf("%d", vMax[i]);

	printf("\n");
	for (int i = 0; i <= k; ++i)
		printf("%d", vMin[i]);

	return 0;
}