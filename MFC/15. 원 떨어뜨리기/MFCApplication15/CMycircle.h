#pragma once
class CMyCircle
{
public:
	CMyCircle();
	~CMyCircle();

	CPoint m_center;
	double m_v;

	void draw(CDC* pDC)
	{
		CBrush b(RGB(255, 0, 0));
		pDC->SelectObject(b);
		pDC->Ellipse(m_center.x - 30, m_center.y - 30, m_center.x + 30, m_center.y + 30);
	}

};

