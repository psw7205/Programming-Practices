
// ChildView.cpp: CChildView 클래스의 구현
//

#include "stdafx.h"
#include "MFCApplication3.h"
#include "ChildView.h"

#ifdef _DEBUG
#define new DEBUG_NEW
#endif


// CChildView

CChildView::CChildView()
{
	color = RGB(255, 0, 0);
}

CChildView::~CChildView()
{
}


BEGIN_MESSAGE_MAP(CChildView, CWnd)
	ON_WM_PAINT()
	ON_WM_LBUTTONDOWN()
	ON_WM_LBUTTONUP()
	ON_WM_MOUSEMOVE()
	ON_COMMAND(ID_COLOR_RED, &CChildView::OnColorRed)
	ON_COMMAND(ID_COLOR_GREEN, &CChildView::OnColorGreen)
	ON_COMMAND(ID_COLOR_BLUE, &CChildView::OnColorBlue)
	ON_UPDATE_COMMAND_UI(ID_COLOR_RED, &CChildView::OnUpdateColorRed)
	ON_UPDATE_COMMAND_UI(ID_COLOR_GREEN, &CChildView::OnUpdateColorGreen)
	ON_UPDATE_COMMAND_UI(ID_COLOR_BLUE, &CChildView::OnUpdateColorBlue)
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
	POSITION pos = m_rect.GetHeadPosition();

	while (pos != NULL)
	{
		m_rect.GetNext(pos).draw(&dc);
	}
	
}



void CChildView::OnLButtonDown(UINT nFlags, CPoint point)
{
	m_rect.AddTail(CMyRect(color));
	m_rect.GetTail().setPt1(point);

	SetCapture();

	CWnd::OnLButtonDown(nFlags, point);
}


void CChildView::OnLButtonUp(UINT nFlags, CPoint point)
{
	m_rect.GetTail().setPt2(point);

	ReleaseCapture();
	Invalidate();
	CWnd::OnLButtonUp(nFlags, point);
}


void CChildView::OnMouseMove(UINT nFlags, CPoint point)
{
	if ((MK_LBUTTON & nFlags) != 0)
	{
		m_rect.GetTail().setPt2(point);
		Invalidate();
	}

	CWnd::OnMouseMove(nFlags, point);
}


void CChildView::OnColorRed()
{
	color = RGB(255, 0, 0);
}


void CChildView::OnColorGreen()
{
	color = RGB(0, 255, 0);
}


void CChildView::OnColorBlue()
{
	color = RGB(0, 0, 255);
}


void CChildView::OnUpdateColorRed(CCmdUI *pCmdUI)
{
	if (m_rect.GetTail().m_color == RGB(255, 0, 0))
	{
		pCmdUI->SetCheck(true);
		pCmdUI->Enable(false);
	}
	else
	{
		pCmdUI->Enable(true);
		pCmdUI->SetCheck(false);
	}
}


void CChildView::OnUpdateColorGreen(CCmdUI *pCmdUI)
{
	if (m_rect.GetTail().m_color == RGB(0, 255, 0))
	{
		pCmdUI->SetCheck(true);
		pCmdUI->Enable(false);
	}
	else
	{
		pCmdUI->Enable(true);
		pCmdUI->SetCheck(false);
	}
}


void CChildView::OnUpdateColorBlue(CCmdUI *pCmdUI)
{
	if (m_rect.GetTail().m_color == RGB(0, 0, 255))
	{
		pCmdUI->SetCheck(true);
		pCmdUI->Enable(false);
	}
	else
	{
		pCmdUI->Enable(true);
		pCmdUI->SetCheck(false);
	}
}
