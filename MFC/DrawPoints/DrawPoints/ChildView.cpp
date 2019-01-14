
// ChildView.cpp : implementation of the CChildView class
//

#include "stdafx.h"
#include "DrawPoints.h"
#include "ChildView.h"

#ifdef _DEBUG
#define new DEBUG_NEW
#endif


// CChildView

CChildView::CChildView()
{
	m_bRButton = false;
}

CChildView::~CChildView()
{
}


BEGIN_MESSAGE_MAP(CChildView, CWnd)
	ON_WM_PAINT()
	ON_WM_MOUSEMOVE()
	ON_WM_RBUTTONDOWN()
	ON_WM_RBUTTONUP()
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
	POSITION pos = m_pts.GetHeadPosition();
	while(pos != NULL)
	{
		CPoint pt = m_pts.GetNext(pos);
		//dc.SetPixelV(pt, RGB(0,0,0));
		dc.Rectangle(pt.x-1, pt.y-1, pt.x+1, pt.y+1);
	}

	dc.SelectStockObject(NULL_BRUSH);

	if(m_bRButton == true)
		dc.Rectangle(m_st.x, m_st.y, m_ed.x, m_ed.y);


	CString str;
	str.Format(_T("No. = %d"), m_pts.GetCount());
	dc.TextOut(0,0,str);
}
void CChildView::OnMouseMove(UINT nFlags, CPoint point)
{
	CWnd::OnMouseMove(nFlags, point);
	if(nFlags & MK_LBUTTON)
	{
		m_pts.AddTail(point);
		Invalidate();
	}
	if(nFlags & MK_RBUTTON)
	{
		m_ed = point;
		Invalidate();
	}

}


void CChildView::OnRButtonDown(UINT nFlags, CPoint point)
{
	// TODO: Add your message handler code here and/or call default

	m_st = point;
	m_bRButton = true;
	SetCapture();

	CWnd::OnRButtonDown(nFlags, point);
}


void CChildView::OnRButtonUp(UINT nFlags, CPoint point)
{
	// TODO: Add your message handler code here and/or call default
	m_ed = point;
	m_bRButton = false;
	ReleaseCapture();

	POSITION pos = m_pts.GetHeadPosition();
	while(pos != NULL)
	{
		POSITION p = pos;
		CPoint pt = m_pts.GetNext(pos);
		if(pt.x >= m_st.x && pt.x <= m_ed.x &&
			pt.y >= m_st.y && pt.y <= m_ed.y)
		{
			m_pts.RemoveAt(p);
		}
	}
	Invalidate();

	CWnd::OnRButtonUp(nFlags, point);
}
