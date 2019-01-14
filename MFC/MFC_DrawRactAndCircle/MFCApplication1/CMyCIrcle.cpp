#include "stdafx.h"
#include "CMyCIrcle.h"


CMyCircle::CMyCircle()
{
	m_r = 0.0;
}


CMyCircle::~CMyCircle()
{
}

void CMyCircle::draw(CDC* pDC)
{
	CBrush brush(m_color);
	pDC->SelectObject(brush);

	pDC->Ellipse(m_ct.x - m_r, m_ct.y - m_r, m_ct.x + m_r, m_ct.y + m_r);
}
