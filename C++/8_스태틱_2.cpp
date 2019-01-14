#include<iostream>
#include<string>

using namespace std;

class CStudent
{
private:
	static int totalNum;

	void setNum()
	{
		totalNum++;
		m_num = totalNum;
	}
	int m_num;
public:
	CStudent()
	{
		setNum();
	}
	void print()
	{
		cout << m_num << endl;
	}
	static int getTotal() { return totalNum;  }
	// 스태틱 함수도 가능 함수들을 관리할 때 사용
	// class는 선언이기 때문에 이런 변수가 있다는 것만 알려줌, main에서 사용해야 메모리가 잡힘
};	// C 언어에서만 이럼... 
	// private에서 작성하면 보호가능, 보호한다면 함수로 접근해야함

int CStudent::totalNum = 0; // totalNum의 소속이 CStudent라고 밖에 따로 구현해줘야함

void func()
{
	cout << "총 숫자 " << CStudent::getTotal(); << endl;
} // 전역함수이기 때문에 클래스 밖에서도 CStudent::totalNum로 접근 가능

int main()
{
	CStudent a, b, c;
	CStudent arr[10];
	CStudent d, e;
	c.print();
	d.print();

	//cout << "총 숫자 " << a.totalNum << " " << b.totalNum << " " << d.totalNum << endl;
	func();

	return 0;
}
