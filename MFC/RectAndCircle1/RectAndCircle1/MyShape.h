#pragma once
class CMyShape
{
public:
	CMyShape(void);
	virtual ~CMyShape(void);
	virtual void draw(CDC * pDC)=0;
	virtual void setPt1(CPoint pt) = 0;
	virtual void setPt2(CPoint pt){};

	COLORREF m_color;
};

