
// ChildView.cpp : implementation of the CChildView class
//

#include "stdafx.h"
#include "RectAndCircle1.h"
#include "ChildView.h"

#ifdef _DEBUG
#define new DEBUG_NEW
#endif

#include "MyCircle.h"
#include "MyRect.h"

// CChildView

CChildView::CChildView()
{
}

CChildView::~CChildView()
{
	POSITION pos = m_shapes.GetHeadPosition();
	while(pos != NULL)
		delete m_shapes.GetNext(pos);


}


BEGIN_MESSAGE_MAP(CChildView, CWnd)
	ON_WM_PAINT()
	ON_WM_LBUTTONDOWN()
	ON_WM_LBUTTONUP()
	ON_WM_RBUTTONDOWN()
	ON_WM_RBUTTONUP()
	ON_WM_MOUSEMOVE()
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

	POSITION pos = m_shapes.GetHeadPosition();
	while(pos!=NULL)
	{
//		CMyShape * pShape = m_shapes.GetNext(pos);
//		pShape->draw(&dc);
		m_shapes.GetNext(pos)->draw(&dc);
	}	
}


void CChildView::OnLButtonDown(UINT nFlags, CPoint point)
{
	CWnd::OnLButtonDown(nFlags, point);
	m_shapes.AddTail(new CMyRect());
	m_shapes.GetTail()->setPt1(point);
	SetCapture();
}
void CChildView::OnLButtonUp(UINT nFlags, CPoint point)
{
	CWnd::OnLButtonUp(nFlags, point);
	m_shapes.GetTail()->setPt2(point);
	ReleaseCapture();
	Invalidate();
}
void CChildView::OnRButtonDown(UINT nFlags, CPoint point)
{
	CWnd::OnRButtonDown(nFlags, point);
	m_shapes.AddTail(new CMyCircle());
	m_shapes.GetTail()->setPt1(point);
	SetCapture();
}

void CChildView::OnRButtonUp(UINT nFlags, CPoint point)
{
	CWnd::OnRButtonUp(nFlags, point);
	m_shapes.GetTail()->setPt2(point);
	ReleaseCapture();
	Invalidate();
}


void CChildView::OnMouseMove(UINT nFlags, CPoint point)
{
	CWnd::OnMouseMove(nFlags, point);
	if((nFlags & MK_LBUTTON) || (nFlags & MK_RBUTTON))
	{
		m_shapes.GetTail()->setPt2(point);
		Invalidate();
	}

}
