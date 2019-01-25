#pragma warning (disable:4996)
#include <bits/stdc++.h>
using namespace std;

int main()
{
	int n;

	scanf("%d", &n);

	int* ar = new int[n];

	for (int i = 0; i < n; ++i)
	{
		scanf("%d", &ar[i]);
	}

	int addPoint = 0;
	int result = 0;
	for (int i = 0; i < n; ++i)
	{
		if (ar[i] == 1)
			addPoint++;
		else
			addPoint = 0;

		result += addPoint;
	}

	printf("%d", result);
	
	delete[] ar;

	return 0;
}