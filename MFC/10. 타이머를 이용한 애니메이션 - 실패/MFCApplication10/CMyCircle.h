#pragma once
class CMyCircle
{
public:
	CMyCircle();
	~CMyCircle();

	CPoint m_center;
	int m_r;
	COLORREF m_color;

	void draw(CDC* pDC) 
	{ 
		CBrush b(m_color);
		pDC->SelectObject(b);
		pDC->Ellipse(m_center.x - m_r, m_center.y - m_r,
			m_center.x + m_r, m_center.y + m_r);
	}

	void setCenter(int x, int y)
	{
		m_center.x = x; 
		m_center.y = y;
	}
};

