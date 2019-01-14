#include <iostream>
using namespace std;

class CCircle
{
public:
	CCircle()
	{
		m_x = 0; m_y = 0;
		m_r = 1;
		cout << "a circle is creationg" << endl;
	}
	~CCircle()
	{
		cout << "a circle is dying" << endl;
	}

	double m_x, m_y;
	double m_r;
	void setRadius(double in_r); // 함수 선언부 declaration, prototype
	
	double getRadius()
	{ 
		return m_r;
	}
	
	//double getCenter() { return x, y; } // 리턴 2개 불가능 
	double getCenter(double *x, double *y)
	{
		*x = m_x;
		*y = m_y;
	}
	/*
	bool isBig(CCircle * a) // 클래스를 받을 땐 포인터나
	{
		if (m_r > a->m_r) return true;
		return false;
	}
	*/
	bool isBig(CCircle & a) // 레퍼런스로 받는다, 레퍼런스로 받으면 새로 만들어지지 않고 main함수의 인자를 그대로 사용함
	{
		if (m_r > a.m_r) return true;
		return false;
	}
	
	CCircle & getMe()
	{
		return *this;
	} // 자기자신을 넘겨줄 땐 레퍼런스 사용 

	double & getX()
	{
		return m_x;
	}

};

void CCircle::setRadius(double in_r) // 정의, 구현부 definition, implimentation
{
	m_r = in_r;
}


int main()
{
	CCircle a, b;
	a.m_r = 1;
	CCircle & r = a; // referencing 별명을 만들어줌, 별명은 항상 이름이 있어야 하고 그냥 선언 불가, 레퍼런스 변수가 있다면 반듯이 값이 있는 상태임
	/*
	CCircle & r;
	r = a; // 불가능, 문법적으로 막혀있음
	*/

	r.m_r = 10; //a.m_r의 값이 10으로 변함
	
	/*
	CCIrcle b = a; // 생성자 없이 바로 복사 됨, 나중에 소멸자만 불림
	와
	CCIrcle b;
	b = a;
	두개는 완전 다른 수행이 일어남
	*/

	/*
	a.setRadius(10);
	b.setRadius(20);

	double x, y;
	double r;
	r = a.getRadius();
	a.getCenter(&x, &y);
	*/

	if (a.isBig(b) == true) cout << "a is bigger than b" << endl;
	else cout << "b is bigger than a" << endl;

	double x = a.getMe().getMe().m_x;


	return 0;
}
