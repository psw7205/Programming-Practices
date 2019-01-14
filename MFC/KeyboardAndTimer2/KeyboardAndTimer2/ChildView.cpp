
// ChildView.cpp : implementation of the CChildView class
//

#include "stdafx.h"
#include "KeyboardAndTimer2.h"
#include "ChildView.h"

#ifdef _DEBUG
#define new DEBUG_NEW
#endif


// CChildView

CChildView::CChildView()
{
	m_r = 50;
	m_x = 200;
	m_y = 200;
	m_dx = 0;
	m_dy = 0;

}

CChildView::~CChildView()
{
}


BEGIN_MESSAGE_MAP(CChildView, CWnd)
	ON_WM_PAINT()
	ON_WM_KEYDOWN()
	ON_WM_CHAR()
	ON_WM_CREATE()
	ON_WM_TIMER()
END_MESSAGE_MAP()



// CChildView message handlers

BOOL CChildView::PreCreateWindow(CREATESTRUCT& cs) 
{
	if (!CWnd::PreCreateWindow(cs))
		return FALSE;

	cs.dwExStyle |= WS_EX_CLIENTEDGE;
	cs.style &= ~WS_BORDER;
	cs.lpszClass = AfxRegisterWndClass(CS_HREDRAW|CS_VREDRAW|CS_DBLCLKS, 
		::LoadCursor(NULL, IDC_ARROW), reinterpret_cast<HBRUSH>(COLOR_WINDOW+1), NULL);

	return TRUE;
}

void CChildView::OnPaint() 
{
	CPaintDC dc(this); // device context for painting
	dc.Ellipse(m_x-m_r,m_y-m_r, m_x+m_r, m_y+m_r);
	dc.TextOutW(0,0, m_str);
}

void CChildView::OnKeyDown(UINT nChar, UINT nRepCnt, UINT nFlags)
{
	CWnd::OnKeyDown(nChar, nRepCnt, nFlags);

	TRACE("nChar = %d nRepCnt = %d \n ", nChar, nRepCnt);
	
	switch(nChar)
	{
	case VK_PRIOR:		m_r += 10;				break;	// PgUp
	case VK_NEXT:		m_r -= 10;				break;	// PgDn
	case VK_UP:			m_dx = 0;  m_dy =-10;	break;
	case VK_DOWN:		m_dx = 0;  m_dy = 10;	break;
	case VK_LEFT:		m_dx =-10; m_dy = 0;	break;
	case VK_RIGHT:		m_dx = 10; m_dy = 0;	break;
	default:									break;
	}

	Invalidate();
}
void CChildView::OnChar(UINT nChar, UINT nRepCnt, UINT nFlags)
{
	CWnd::OnChar(nChar, nRepCnt, nFlags);
/*
	int a = 'a';
	string str;
	str += char(a);
*/
	if(nChar == VK_BACK)
		m_str.Delete(m_str.GetLength()-1, 1);
	else 
		m_str += TCHAR(nChar);

	Invalidate();

}


int CChildView::OnCreate(LPCREATESTRUCT lpCreateStruct)
{
	if (CWnd::OnCreate(lpCreateStruct) == -1)
		return -1;

	// TODO:  Add your specialized creation code here
	SetTimer(0, 1, NULL);
	return 0;
}

void CChildView::OnTimer(UINT_PTR nIDEvent)
{
	m_x += m_dx;
	m_y += m_dy;
	
	CRect rect;
	GetClientRect(rect);
	if(m_x+m_r > rect.right)
	{
		m_x = rect.right-m_r;
		m_dx = - m_dx;
	}
	if(m_x-m_r <rect.left)
	{
		m_x = rect.left + m_r;
		m_dx = - m_dx;
	}

	Invalidate();

	CWnd::OnTimer(nIDEvent);
}
