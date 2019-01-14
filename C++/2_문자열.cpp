#include<iostream>
#include<cstring>
#include<string>

using namespace std;

int mystrlen(const char s[])
{
	int l = 0;
	while (true)
	{
		if (s[l] == 0) 
			break;
		l++;
	}

	return l;
}


int main()
{
	char c;

	c = 'a';
	cout << c << endl;
	cout << int(c) << endl;

	char ar[10] = "abc" ; // {'a','b','c', 0 };
	ar[0] = 'a';
	ar[1] = 'b';
	ar[2] = 'c';
	ar[3] = 0 ; // Null character 맨 마지막에 필수


	cout << strlen(ar) << endl;
	cout << ar << endl;
	cout << mystrlen("sejong") << endl; //strlen()함수를 모를 때 만들어서 사용

	char name[100];
	cout << "이름" << endl;
	cin >> name; // 문자열에서 공백이 있으면 공백 뒤로는 못 저장함
	cin.getline(name, 100); // name 변수에 최대 100글자 까지 넣어라, 공백까지 포함해서 저장

	cout << "당신의 이름은 " << name << "입니다" << endl;

	// 아스키코드 : 1 바이트, 한글 X, 오직 영어만 c, c++, c#
	// 유니코드 : 2 바이트, 모든 언어 자바 , 파이썬


	string str = "ABC" ; // c++에서 제공하는 문자열 타입 #include<string>필요
	str = "sejong"; // char 배열 이용한 문자열 저장에선 불가능한 방법

	string str1 = "university";
	string str2 = str + str1;
	string str3;

	cin >> str3; 

	cout << str2 << endl;
	cout << str2.length() << endl; //문자열 길이도 바로 출력가능

	return 0;
}
