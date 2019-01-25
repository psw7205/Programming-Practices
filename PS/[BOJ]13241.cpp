#include <bits/stdc++.h>
using namespace std;

long long gcd(int a, int b)
{
	if (a % b == 0)
		return b;

	return gcd(b, a%b);
}

long long lcm(int a, int b)
{
	return (long long)a * b / gcd(a, b);
}

int main()
{
	int n, m;
	long long result = 0;
	scanf("%d %d", &n, &m);

	result = lcm(n, m);
	printf("%lld", result);

	return 0;
}