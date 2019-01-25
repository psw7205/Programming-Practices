#include <bits/stdc++.h>
using namespace std;

int n, a[100001];

stack<int> s;
vector<char> ans;

int main() 
{
	scanf("%d", &n);
	for (int i = 0; i < n; i++) 
		scanf("%d", &a[i]);

	int pos = 0;

	for (int i = 1; i <= n; i++) 
	{
		s.push(i);
		ans.push_back('+');
		while (!s.empty() && s.top() == a[pos]) 
		{
			pos++;
			s.pop();
			ans.push_back('-');
		}
	}

	if (!s.empty()) 
		puts("NO");
	else 
		for (auto it : ans) 
			printf("%c\n", it);

	return 0;
}