#pragma once
#include "CMyShape.h"
#include <cmath>
class CMyCircle :
	public CMyShape
{
public:
	CMyCircle();
	~CMyCircle();
	void draw(CDC* pDC);
	void setPt1(CPoint pt) { m_ct = pt; }
	void setPt2(CPoint pt) 
	{
		m_r = (m_ct.x - pt.x)*(m_ct.x - pt.x) + (m_ct.y - pt.y)*(m_ct.y - pt.y);
		m_r = sqrt(m_r);
	}

	CPoint m_ct;
	double m_r;
};

