
// ChildView.cpp: CChildView 클래스의 구현
//

#include "stdafx.h"
#include "MFCApplication3_2.h"
#include "ChildView.h"

#ifdef _DEBUG
#define new DEBUG_NEW
#endif


// CChildView

CChildView::CChildView()
{
	m_flag = false;
}

CChildView::~CChildView()
{
	POSITION pos = m_rect.GetHeadPosition();
	while (pos != NULL)
		delete m_rect.GetNext(pos);
}


BEGIN_MESSAGE_MAP(CChildView, CWnd)
	ON_WM_PAINT()
	ON_WM_LBUTTONDOWN()
	ON_WM_LBUTTONUP()
	ON_WM_MOUSEMOVE()
END_MESSAGE_MAP()



// CChildView 메시지 처리기

BOOL CChildView::PreCreateWindow(CREATESTRUCT& cs)
{
	if (!CWnd::PreCreateWindow(cs))
		return FALSE;

	cs.dwExStyle |= WS_EX_CLIENTEDGE;
	cs.style &= ~WS_BORDER;
	cs.lpszClass = AfxRegisterWndClass(CS_HREDRAW | CS_VREDRAW | CS_DBLCLKS,
		::LoadCursor(nullptr, IDC_ARROW), reinterpret_cast<HBRUSH>(COLOR_WINDOW + 1), nullptr);

	return TRUE;
}

void CChildView::OnPaint()
{
	CPaintDC dc(this);

	dc.TextOutW(0, 0, _T("16013093 박상우"));

	POSITION pos = m_rect.GetHeadPosition();

	while (pos)
	{
		m_rect.GetNext(pos)->draw(&dc);
	}
}



void CChildView::OnLButtonDown(UINT nFlags, CPoint point)
{
	POSITION pos = m_rect.GetTailPosition();

	while (pos)
	{
		if (m_rect.GetAt(pos)->m_st.x < point.x && m_rect.GetAt(pos)->m_ed.x > point.x
			&& m_rect.GetAt(pos)->m_st.y > point.y && m_rect.GetAt(pos)->m_ed.y < point.y)
		{
			m_tmp1 = m_rect.GetAt(pos)->m_st - point;
			m_tmp2 = m_rect.GetAt(pos)->m_ed - point;
			m_flag = true;
			m_rect.GetAt(pos)->m_color = RGB(255, 255, 0);
			m_pos = pos;
			Invalidate();
			break;
		}

		m_rect.GetPrev(pos);
		m_flag = false;
	}

	if (m_flag == false)
	{
		m_rect.AddTail(new CMyRect());
		m_rect.GetTail()->m_st = point;
		SetCapture();
	}

	CWnd::OnLButtonDown(nFlags, point);
}


void CChildView::OnLButtonUp(UINT nFlags, CPoint point)
{
	if (m_flag == false)
	{
		m_rect.GetTail()->m_ed = point;

		if (m_rect.GetTail()->m_st.x - m_rect.GetTail()->m_ed.x > 0)
		{
			int tmp = m_rect.GetTail()->m_ed.x;
			m_rect.GetTail()->m_ed.x = m_rect.GetTail()->m_st.x;
			m_rect.GetTail()->m_st.x = tmp;
		}

		if (m_rect.GetTail()->m_st.y - m_rect.GetTail()->m_ed.y < 0)
		{
			int tmp = m_rect.GetTail()->m_ed.y;
			m_rect.GetTail()->m_ed.y = m_rect.GetTail()->m_st.y;
			m_rect.GetTail()->m_st.y = tmp;
		}

		ReleaseCapture();
		Invalidate();
	}

	if (m_flag == true)
	{
		m_flag = false;
		m_rect.GetAt(m_pos)->m_color = RGB(255, 255, 255);
		Invalidate();
	}

	CWnd::OnLButtonUp(nFlags, point);
}


void CChildView::OnMouseMove(UINT nFlags, CPoint point)
{

	if (nFlags & MK_LBUTTON && m_flag == true)
	{
		m_rect.GetAt(m_pos)->m_st = point + m_tmp1;
		m_rect.GetAt(m_pos)->m_ed = point + m_tmp2;
		Invalidate();
	}

	if (nFlags & MK_LBUTTON && m_flag == false)
	{
		m_rect.GetTail()->m_ed = point;
		Invalidate();
	}

	CWnd::OnMouseMove(nFlags, point);
}
