#include "stdafx.h"
#include "CMyCircle.h"


CMyCircle::CMyCircle()
{
	m_r = 0;
}


CMyCircle::~CMyCircle()
{
}

void CMyCircle::draw(CDC* pDC)
{
	pDC->Ellipse(m_pt.x - m_r, m_pt.y - m_r, m_pt.x + m_r, m_pt.y + m_r);
}