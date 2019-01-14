#pragma once
#include "myshape.h"
class CMyRect :
	public CMyShape
{
public:
	CMyRect(void);
	~CMyRect(void);
	void draw(CDC * pDC);
	void setPt1(CPoint pt) { m_pt1 = pt;}
	void setPt2(CPoint pt) { m_pt2 = pt;}

	CPoint m_pt1, m_pt2;
};

