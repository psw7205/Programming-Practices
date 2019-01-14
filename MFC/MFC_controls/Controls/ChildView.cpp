
// ChildView.cpp : implementation of the CChildView class
//

#include "stdafx.h"
#include "Controls.h"
#include "ChildView.h"

#ifdef _DEBUG
#define new DEBUG_NEW
#endif


// CChildView

CChildView::CChildView()
{
}

CChildView::~CChildView()
{
}


BEGIN_MESSAGE_MAP(CChildView, CWnd)
	ON_WM_PAINT()
	ON_WM_CREATE()
	ON_WM_LBUTTONDOWN()
	ON_BN_CLICKED(101, OnButtonClicked)
	ON_BN_CLICKED(102, OnCheck1Clicked)
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
	
	// TODO: Add your message handler code here
	if(m_check1.GetCheck()==true)
		dc.Ellipse(100,100,400,400);

	// Do not call CWnd::OnPaint() for painting messages
}



int CChildView::OnCreate(LPCREATESTRUCT lpCreateStruct)
{
	if (CWnd::OnCreate(lpCreateStruct) == -1)
		return -1;

	// TODO:  Add your specialized creation code here

	m_button.Create(_T("Test"), 
		WS_CHILD|WS_VISIBLE|BS_PUSHBUTTON,
		       CRect(100,100,200,150), this, 101);

	m_check1.Create(_T("자료구조"),
		WS_CHILD|WS_VISIBLE|BS_CHECKBOX,
		       CRect(100,150,200,200), this, 102);

	m_check2.Create(_T("C++"),
		WS_CHILD|WS_VISIBLE|BS_AUTOCHECKBOX,
		       CRect(100,200,200,250), this, 103);

	CString str[3] = {_T("2학년"), _T("3학년"), _T("4학년")};
	for(int i=0; i<3; i++)
		m_radio[i].Create(str[i],
				WS_CHILD|WS_VISIBLE|BS_AUTORADIOBUTTON,
				CRect(100,300+50*i,200,300+50*(i+1)), 
				this, 104+i);



	return 0;
}


void CChildView::OnLButtonDown(UINT nFlags, CPoint point)
{
	// TODO: Add your message handler code here and/or call default

	if(m_button.IsWindowVisible()==true)
		m_button.ShowWindow(false);
	else
		m_button.ShowWindow(true);


	CWnd::OnLButtonDown(nFlags, point);
}

void CChildView::OnButtonClicked()
{
	CString str = _T("수강과목: \n");
	if(m_check1.GetCheck()==true)
		str += _T("자료구조 \n");
	if(m_check2.GetCheck()==true)
		str += _T("C++ \n");
	str += _T(" \n");
	str += _T("학년: \n");
	for(int i=0; i<3; i++)
		if(m_radio[i].GetCheck()==true)
		{
			CString str1;
			m_radio[i].GetWindowText(str1);
			str += str1;
		}
	MessageBox(str);
}

void CChildView::OnCheck1Clicked()
{
	m_check1.SetCheck(!m_check1.GetCheck());

	if(m_check1.GetCheck() == true)
		m_check2.SetCheck(true);

	Invalidate();
}