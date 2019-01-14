#pragma once
class MouseTrace
{
public:
	MouseTrace();
	MouseTrace(CPoint p);
	~MouseTrace();

	CPoint m_pt;
	COLORREF m_color;
	int m_r;

	void draw(CDC* pDC)
	{
		CBrush b(m_color);
		pDC->SelectObject(b);
		pDC->Ellipse(m_pt.x - m_r, m_pt.y - m_r, m_pt.x + m_r, m_pt.y + m_r);
	}
};

