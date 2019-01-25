#include <bits/stdc++.h>

using namespace std;



int main()

{

	char a[10001] = { 0 };
	char b[10001] = { 0 };

	char result[10001] = { 0 };



	scanf("%s %s", a, b);



	int len = min(strlen(a), strlen(b));



	std::reverse(a, a + strlen(a));

	std::reverse(b, b + strlen(b));



	int sum = 0;

	int carry = 0;

	for (int i = 0; i < len; ++i)

	{

		sum = a[i] + b[i] - '0' - '0' + carry;

		carry = 0;

		if (sum >= 10)

		{

			carry = 1;

			sum %= 10;

		}

		

		result[i] = sum + '0';

	}



	if (strlen(a) == len)

	{

		for (int i = len; i < strlen(b); ++i)

		{

			sum = b[i] - '0' + carry;

			carry = 0;

			if (sum >= 10)

			{

				carry = 1;

				sum %= 10;

			}



			result[i] = sum + '0';

		}

	}

	

	if (strlen(b) == len)

	{

		for (int i = len; i < strlen(a); ++i)

		{

			sum = a[i] - '0' + carry;

			carry = 0;

			if (sum >= 10)

			{

				carry = 1;

				sum %= 10;

			}



			result[i] = sum + '0';

		}

	}



	if (carry == 1)

	{

		int tmp = strlen(result);

		result[tmp] = 1 + '0';

		result[tmp + 1] = 0;

	}



	std::reverse(result, result + strlen(result));



	printf("%s", result);



	return 0;

}