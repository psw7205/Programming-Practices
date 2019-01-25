#include <bits/stdc++.h>
using namespace std;

bool prime[250000];

int main()
{
	memset(prime, 1, sizeof(prime));
	prime[0] = prime[1] = 0;

	for (int i = 2; i < 250000; ++i)
	{
		if (prime[i] == true)
		{
			int j = i + i;
			while (j < 250000)
			{
				prime[j] = false;
				j += i;
			}
		}
	}


	while (true)
	{
		int num;
		scanf("%d", &num);

		if (num == 0)
		{
			break;
		}

		int n = 0;
		
		for (int i = num + 1; i <= num * 2; ++i)
		{
			if (prime[i] == true)
				n++;
		}

		printf("%d\n", n);
	}

	return 0;
}