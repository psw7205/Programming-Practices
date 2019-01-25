#include <bits/stdc++.h>
using namespace std;

int main()
{
	int n;
	cin >> n;

	while (n--)
	{

		stack<char> s;

		string str;
		cin >> str;

		bool flag = false;

		for (int i = 0; i < str.size(); ++i)
		{
			if (str[i] == '(')
				s.push(str[i]);

			if (str[i] == ')')
			{
				if (s.size() == 0)
				{
					cout << "NO" << endl;
					flag = true;
					break;
				}

				s.pop();
			}
		}

		if (s.size() == 0 && flag != true)
			cout << "YES" << endl;
		else if (flag == true)
			continue;
		else
			cout << "NO" << endl;
	}
	return 0;
}