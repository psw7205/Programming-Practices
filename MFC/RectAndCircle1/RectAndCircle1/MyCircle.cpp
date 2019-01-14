#include "StdAfx.h"
#include "MyCircle.h"


CMyCircle::CMyCircle(void)
{
	m_r = 0;
}

CMyCircle::~CMyCircle(void)
{
}

void CMyCircle::draw(CDC * pDC)
{
	CBrush brush(m_color);
	pDC->SelectObject(brush);

	pDC->Ellipse
		(m_pt.x-m_r, m_pt.y-m_r,m_pt.x+m_r, m_pt.y+m_r);

}

