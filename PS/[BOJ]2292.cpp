#include <bits/stdc++.h>
using namespace std;

int main()
{
	int n;
	scanf("%d", &n);

	if (n == 1)
	{
		printf("1");
		return 0;
	}

	int i = 0;
	int max = 2;
	while (true)
	{
		int inc = 6 * i + 5;
		max += inc;
		if (max >= n)
		{
			printf("%d", i + 2);
			break;
		}
		else
		{
			max++, i++;
		}
	}

	return 0;
}