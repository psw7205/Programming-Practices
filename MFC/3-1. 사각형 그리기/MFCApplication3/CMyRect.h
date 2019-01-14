#pragma once
class CMyRect
{
public:
	CMyRect() {};
	CMyRect(COLORREF color);
	~CMyRect();

	COLORREF m_color;

	CPoint m_pt1, m_pt2;

	void draw(CDC* pDC);
	void setPt1(CPoint pt) { m_pt1 = pt; }
	void setPt2(CPoint pt) { m_pt2 = pt; }
};

