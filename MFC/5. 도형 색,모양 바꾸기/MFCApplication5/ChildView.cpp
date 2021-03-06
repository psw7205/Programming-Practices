
// ChildView.cpp: CChildView 클래스의 구현
//

#include "stdafx.h"
#include "MFCApplication5.h"
#include "ChildView.h"

#ifdef _DEBUG
#define new DEBUG_NEW
#endif


// CChildView

CChildView::CChildView()
{
	m_flag = CIRCLE;
	m_color = RGB(255, 255, 255);
}

CChildView::~CChildView()
{
}


BEGIN_MESSAGE_MAP(CChildView, CWnd)
	ON_WM_PAINT()
	ON_COMMAND(ID_SHAPE_CIRCLE, &CChildView::OnShapeCircle)
	ON_COMMAND(ID_SHAPE_RECTANGLE, &CChildView::OnShapeRectangle)
	ON_WM_LBUTTONDOWN()
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

	dc.TextOutW(0, 0, _T("16013093 박상우"));
	
	CBrush r(RGB(255, 0, 0));
	CRect rr(30, 40, 150, 100);
	dc.SelectObject(r);

	dc.Rectangle(rr);

	CBrush g(RGB(0, 255, 0));
	CRect rg(180, 40, 300, 100);
	dc.SelectObject(g);

	dc.Rectangle(rg);

	CBrush b(RGB(0, 0, 255));
	CRect rb(330, 40, 450, 100);
	dc.SelectObject(b);

	dc.Rectangle(rb);

	if (CIRCLE == m_flag)
	{
		CBrush c(m_color);
		dc.SelectObject(c);
		dc.Ellipse(20, 200, 700, 880);
	}
	if (RECTANGLE== m_flag)
	{
		CBrush c(m_color);
		dc.SelectObject(c);
		dc.Rectangle(20, 200, 700, 880);
	}

}



void CChildView::OnShapeCircle()
{
	if (m_flag == RECTANGLE)
		m_flag = CIRCLE;
	Invalidate();
}


void CChildView::OnShapeRectangle()
{
	if (m_flag == CIRCLE)
		m_flag = RECTANGLE;
	Invalidate();
}


void CChildView::OnLButtonDown(UINT nFlags, CPoint point)
{
	CWnd::OnLButtonDown(nFlags, point);
	
	if (point.x > 30 && point.y > 40 && point.x < 150 && point.y < 100)
		m_color = RGB(255, 0, 0);

	if (point.x > 180 && point.y > 40 && point.x < 300 && point.y < 100)
		m_color = RGB(0, 255, 0);

	if (point.x > 330 && point.y > 40 && point.x < 450 && point.y < 100)
		m_color = RGB(0, 0, 255);

	Invalidate();
}
