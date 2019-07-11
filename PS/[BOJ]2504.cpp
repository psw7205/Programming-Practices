#include <bits/stdc++.h>
using namespace std;

int main()
{
	stack<char> s;
	string str;
	cin >> str;

	bool isValid = true;
	int op = 1;
	int result = 0;

	for (int i = 0; i < str.length(); ++i)
	{
		if (s.size() == 0 && (str[i] == ']' || str[i] == ')'))
		{
			isValid = false;
			break;
		}

		if (str[i] == ')')
		{
			char tmp = s.top();
			s.pop();

			if (tmp == '[')
			{
				isValid = false;
				break;
			}
			else
			{
				if (str[i - 1] == '(')
					result += op;
				op /= 2;
			}
		}
		else if (str[i] == ']')
		{
			char tmp = s.top();
			s.pop();

			if (tmp == '(')
			{
				isValid = false;
				break;
			}
			else
			{
				if (str[i - 1] == '[')
					result += op;
				op /= 3;
			}
		}
		else
		{
			s.push(str[i]);
			if (str[i] == '(')
			{
				op *= 2;
			}
			else if (str[i] == '[')
			{
				op *= 3;
			}
		}
	}

	if (isValid && s.size() == 0)
		cout << result << endl;
	else
		cout << "0" << endl;

	return 0;
}