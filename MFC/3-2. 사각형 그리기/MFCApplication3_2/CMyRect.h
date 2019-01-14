#pragma once
class CMyRect
{
public:
	CMyRect();
	~CMyRect();

	CPoint m_st, m_ed;
	COLORREF m_color;

	void draw(CDC* pDc);
};