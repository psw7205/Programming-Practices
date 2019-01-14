#include <iostream>
using namespace std;

class CCircle
{
public:
	double m_x, m_y;
	double m_r;
	void setRadius(double in_r, CCircle c)
	{
		m_r = in_r;

		if (isOverlap(c, *this) == true) // 내 객체를 활용해 사용하는 함수의 인풋으로 지기자신를 주고 싶을 때
		{
			m_r == 0;
		}

	}

	/* 1
	double r;
	void setRadius(double r)
	{
		this; // 멤버함수 안에서 자동으로 호출됨 그 주소를 알려줌
		cout << this << endl;
		r = r;
	} // 문제는 없지만 헷갈림, this->r 로 접근해 구분 가능
	*/

};

bool isOverlap(CCircle a, CCircle b)
{
	double dist = (a.m_x - b.m_x)*(a.m_r - b.m_x) + (a.m_y - b.m_y)*(a.m_y - b.m_y);
	dist = sqrt(dist);
	double r2 = a.m_r + b.m_r;
	if (dist > r2)	return true;
	else false;
} // 두 원이 겹치면 true 아니면 false


int main()
{
	CCircle a, b;

	/* 1
	cout << &a << endl;
	cout << &b << endl;
	*/

	a.setRadius(10, b);
	b.setRadius(20, a);


	return 0;
}