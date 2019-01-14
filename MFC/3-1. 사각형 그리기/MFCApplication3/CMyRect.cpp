#include "stdafx.h"
#include "CMyRect.h"


CMyRect::CMyRect(COLORREF color)
{
	m_color = color;
}


CMyRect::~CMyRect()
{
}

void CMyRect::draw(CDC* pDC)
{
	CBrush brush(m_color);
	pDC->SelectObject(brush);
	pDC->Rectangle(m_pt1.x, m_pt1.y, m_pt2.x, m_pt2.y);
}