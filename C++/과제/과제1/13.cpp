#include<iostream>
#include<string>
#pragma warning(disable: 4996)//vs2017버전 strtok의 c4996 오류를 무시

using namespace std;

int main()
{
	while (true)
	{
		char number[100];
		char *p[4];
		int a, b;

		cout << "? " ;
		cin.getline(number, 100);

		p[0] = strtok(number, " "); // 문자열 number를 " "까지 구분

		for (int i = 1; i < 3; i++)
		{
			p[i] = strtok('\0', " "); // 그 다음부터 " "를 구분 반복
		}

		a = atoi(p[0]);
		b = atoi(p[2]); // a, b를 정수로

		cout << a << " " << p[1] << " " << b << " = ";

		if (strcmp(p[1], "+") == 0) a += b;
		if (strcmp(p[1], "-") == 0) a -= b;
		if (strcmp(p[1], "*") == 0) a *= b;
		if (strcmp(p[1], "/") == 0) a /= b;
		if (strcmp(p[1], "%") == 0) a %= b;
		//strcmp를 이용 p[1]과 각 연산자가 같으면 수행

		cout << a << endl;

	}

	return 0;
}
