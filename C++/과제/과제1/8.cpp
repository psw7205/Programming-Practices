#include<iostream>
#include<string>
#pragma warning(disable: 4996)//vs2017버전 strtok의 c4996 오류를 무시

using namespace std;

int main()
{
	char name[100];
	char *p[6];
	int n;
	string longname;

	cout << "5명의 이름을 ';'로 구분하여 입력하세요" << endl << ">>";

	cin.getline(name, 100);

	p[0] = strtok(name, ";"); // 문자열 맨처음 부터 ';'까지 구분

	for (int i = 0; i < 5; i++)
	{
		p[i+1] = strtok('\0',";"); // 그 다음부터 ';'까지 구분 반복 
		cout << i + 1 << " : " << p[i] << endl;
	}

	n = strlen(p[0]); 

	longname = p[0];
	
	for (int i = 1; i < 5; i++)
	{
		if (n < strlen(p[i])) 
		{
			longname = p[i]; 
			break;
		}// 문자열 길이가 더 긴쪽을 longname에 저장
	}

	cout << "가장 긴 이름은 " << longname << endl;


	return 0;
}
