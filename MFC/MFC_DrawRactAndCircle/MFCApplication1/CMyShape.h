#pragma once
class CMyShape
{
public:
	CMyShape();
	virtual ~CMyShape();

	virtual void draw(CDC* pDC) = 0; // 이런 모양의 함수가 필요하다, 추상함수(abstract function), 추상함수가 하나라도 있으면 추상클래스라고 함, 추상클래스는 변수 선언 불가능
	virtual void setPt1(CPoint pt) = 0; // 무조건 다른 클래스에서 구현을 해줘야함
	virtual void setPt2(CPoint pt) {}; // 구현 안해줘도 됨

	COLORREF m_color;
};

