
// ChildView.cpp: CChildView 클래스의 구현
//

#include "stdafx.h"
#include "MFCApplication1.h"
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

	POSITION pos = m_pts.GetHeadPosition();
	while (pos != NULL)
	{
		CPoint pt = m_pts.GetNext(pos);
		dc.Rectangle(pt.x - 1, pt.y - 1, pt.x + 1, pt.y + 1);
	}

	dc.SelectStockObject(NULL_BRUSH);
	
	CPen pen(PS_SOLID, 1, RGB(255, 0, 0));
	dc.SelectObject(pen);

	if(m_bRButton == true)
		dc.Rectangle(m_st.x, m_st.y, m_ed.x, m_ed.y);

	CString str;
	str.Format(_T("총 점의 갯수 = %d"), m_pts.GetCount());
	dc.TextOutW(0, 30, str);
}



void CChildView::OnMouseMove(UINT nFlags, CPoint point)
{
	CWnd::OnMouseMove(nFlags, point);

	if (nFlags & MK_LBUTTON)
	{
		m_pts.AddTail(point);
		Invalidate();
	}
	if (nFlags & MK_RBUTTON)
	{
		m_ed = point;
		Invalidate();
	}
}


void CChildView::OnRButtonDown(UINT nFlags, CPoint point)
{
	m_st = point;
	m_bRButton = true;
	SetCapture();

	CWnd::OnRButtonDown(nFlags, point);
}


void CChildView::OnRButtonUp(UINT nFlags, CPoint point)
{
	m_ed = point;
	m_bRButton = false;
	ReleaseCapture();

	if (m_st.x > m_ed.x)
	{
		int tmp = m_st.x;
		m_st.x = m_ed.x;
		m_ed.x = tmp;
	}

	if (m_st.y > m_ed.y)
	{
		int tmp = m_st.y;
		m_st.y = m_ed.y;
		m_ed.y = tmp;
	}

	POSITION pos = m_pts.GetHeadPosition();
	while (pos != NULL)
	{
		POSITION p = pos;
		CPoint pt = m_pts.GetNext(pos);
		if (pt.x >= m_st.x && pt.x <= m_ed.x &&
			pt.y >= m_st.y && pt.y <= m_ed.y)
		{
			m_pts.RemoveAt(p);
		}

	}
	Invalidate();

	CWnd::OnRButtonUp(nFlags, point);
}
