#include <bits/stdc++.h>
using namespace std;

int ar[100000];

int gcd(int a, int b)
{
	if (a % b == 0)
		return b;

	return gcd(b, a%b);
}

int lcm(int a, int b)
{
	return a * b / gcd(a, b);
}

int main()
{
	int a, b, c, d;
	scanf("%d %d %d %d", &a, &b, &c, &d);

	int numerator, denominator;
	denominator = lcm(b, d);
	numerator = a * (denominator / b) + c * (denominator / d);
	
	int g = gcd(denominator, numerator);

	printf("%d %d", numerator / g, denominator / g);

	return 0;
}