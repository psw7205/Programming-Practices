#include "stdafx.h"
#include "mouseTrace.h"


MouseTrace::MouseTrace()
{
	m_r = 0;
	m_color = RGB(0, 0, 0);
}

MouseTrace::MouseTrace(CPoint p)
{
	m_pt = p;
	m_r = 0;
	m_color = RGB(0, 0, 0);
}

MouseTrace::~MouseTrace()
{
}
