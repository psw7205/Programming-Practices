#include<stdio.h> // C표준, C++표준은 <cstdio>
#include<iostream> // input output stream
using namespace std;

namespace sejong // namespace 선언방식
{
	int a = 5;
}


int main()
{

	printf("hellow world\n");


	std::cout << "hellow world\n";
	//console out, 전역변수
	//standard에 속한 cout이라는 변수

	char s[] = "world!";
	int a = 10;
	std::cout << "hellow " << s << a << std::endl ;
	// 모니터에 hellow먼저 보내고 s보내고 a를 보냄
	printf("hellow %s %f \n", s, a); // %f처럼 자로형 실수가 없어짐
	// std::endl == \n
	
	// A::B -> A namespace에 B가 소속되어있다

	//3번줄 선언시 std::생략가능
	//#inclued<iostream>과 using namespace std;는 항상 고정
	cout << "hellow " << s << a << endl;
	cout << sejong::a << endl;



	return 0;
}