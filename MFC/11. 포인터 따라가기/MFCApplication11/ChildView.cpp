
// ChildView.cpp: CChildView 클래스의 구현
//

#include "stdafx.h"
#include "MFCApplication11.h"
#include "ChildView.h"

#ifdef _DEBUG
#define new DEBUG_NEW
#endif


// CChildView

CChildView::CChildView()
{
	m_dr = 1;
	m_flag = 0;
}

CChildView::~CChildView()
{
}


BEGIN_MESSAGE_MAP(CChildView, CWnd)
	ON_WM_PAINT()
	ON_WM_MOUSEMOVE()
	ON_WM_CREATE()
	ON_WM_TIMER()
END_MESSAGE_MAP()



// CChildView 메시지 처리기

BOOL CChildView::PreCreateWindow(CREATESTRUCT& cs) 
{
	if (!CWnd::PreCreateWindow(cs))
		return FALSE;

	cs.dwExStyle |= WS_EX_CLIENTEDGE;
	cs.style &= ~WS_BORDER;
	cs.lpszClass = AfxRegisterWndClass(CS_HREDRAW|CS_VREDRAW|CS_DBLCLKS, 
		::LoadCursor(nullptr, IDC_ARROW), reinterpret_cast<HBRUSH>(COLOR_WINDOW+1), nullptr);

	return TRUE;
}

void CChildView::OnPaint() 
{
	CPaintDC dc(this); 

	m_mouse.draw(&dc);
}



void CChildView::OnMouseMove(UINT nFlags, CPoint point)
{
	m_mouse.m_pt = point;
	Invalidate();

	CWnd::OnMouseMove(nFlags, point);
}


int CChildView::OnCreate(LPCREATESTRUCT lpCreateStruct)
{
	if (CWnd::OnCreate(lpCreateStruct) == -1)
		return -1;

	SetTimer(0, 1, NULL);

	return 0;
}


void CChildView::OnTimer(UINT_PTR nIDEvent)
{
	if (nIDEvent == 0)
	{
		m_mouse.m_color = RGB(m_dr, m_dr, m_dr);
		
		if (m_flag == 0)
		{
			m_mouse.m_r = m_dr++;
			if (m_dr == 50)
				m_flag = 1;
		}
		
		if (m_flag == 1)
		{
			m_mouse.m_r = m_dr--;
			if (m_dr == 0)
				m_flag = 0;
		}

		Invalidate();
	}

	CWnd::OnTimer(nIDEvent);
}
