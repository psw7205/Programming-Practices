#include<iostream>
#include<string>

using namespace std;

/*
int cnt = 0;
void func() // cnt나 func() 둘중 하나라도 없으면 안돌아감, 서로 종속되어있음.
{
	cnt++;

	if(cnt % 2 == 1)
		cout << "홀" << endl;
	else
		cout << "짝" << endl;
}
*/
void func() 
{
	static int cnt = 0; // 함수 속에서 선언되는 전역변수 이 함수에서만 읽을 수 있음
	cnt++;				// 함수가 실행되기 전에 미리 생성됨 여러번 함수를 호출해도 static은 딱 1번만 불림
	if (cnt % 2 == 1)
		cout << "홀" << endl;
	else
		cout << "짝" << endl;
}

int main()
{
	func();
	func();
	func();
	func();

	return 0;
}
