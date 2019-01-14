#pragma once
#include "myshape.h"
#include <cmath>

class CMyCircle :
	public CMyShape
{
public:
	CMyCircle(void);
	~CMyCircle(void);
	void draw(CDC * pDC);
	void setPt1(CPoint pt) {m_pt = pt;}
	void setPt2(CPoint pt)
	{
		m_r = (m_pt.x-pt.x)*(m_pt.x-pt.x)
			 +(m_pt.y-pt.y)*(m_pt.y-pt.y);
		m_r = sqrt(m_r);
	}

	CPoint m_pt;
	float m_r;
};

