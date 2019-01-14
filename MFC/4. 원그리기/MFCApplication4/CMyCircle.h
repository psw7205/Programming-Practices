#pragma once
class CMyCircle
{
public:
	CMyCircle();
	~CMyCircle();

	double m_r;
	CPoint m_pt;

	void draw(CDC* pDC);
	void setPt1(CPoint pt) { m_pt= pt; }
	void setPt2(CPoint pt)
	{
		m_r = (m_pt.x - pt.x)*(m_pt.x - pt.x)
			+ (m_pt.y - pt.y)*(m_pt.y - pt.y);
		m_r = sqrt(m_r);
	}
};

