#include "stdafx.h"
#include "CMyRect.h"


CMyRect::CMyRect()
{
	m_color = RGB(255, 255, 255);
}


CMyRect::~CMyRect()
{
}


void CMyRect::draw(CDC* pDC)
{
	CBrush brush(m_color);
	pDC->SelectObject(brush);
	pDC->Rectangle(m_st.x, m_st.y, m_ed.x, m_ed.y);
}