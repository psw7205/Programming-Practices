
// ChildView.cpp : implementation of the CChildView class
//

#include "stdafx.h"
#include "MoreDraw2.h"
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
	
	CBitmap bmp;
	bmp.LoadBitmap(IDB_BITMAP1);
	CBrush BkBrush(&bmp);
	dc.SelectObject(BkBrush);

	CRect rect;
	GetClientRect(rect);
	dc.Rectangle(rect);

	CPen pen1(PS_SOLID, 3, RGB(0,0,255));
	CPen pen2(PS_DASH, 1, RGB(255,0,255));
	CBrush brush1(RGB(255,255,200));
	CBrush brush2(HS_DIAGCROSS, RGB(0,0,0));
	
	CFont font;
	font.CreatePointFont(200, _T("HY¿±¼­M"));
	
	//dc.SelectObject(pen1);
	dc.SelectStockObject(NULL_PEN);
	dc.SelectObject(brush1);
	dc.SelectObject(font);
	// TODO: Add your message handler code here
	dc.Rectangle(150,50,250,250);

	dc.SetTextColor(RGB(255,255,255));
	dc.SetBkColor(RGB(200,200,200));
	dc.SetTextAlign(TA_LEFT);
	dc.SetBkMode(TRANSPARENT);
	//dc.SetBkMode(OPAQUE);
//	COLORREF c = dc.GetTextColor();
	dc.TextOut(100,100, _T("á¦ðóÓÞùÊÎè"));
	dc.TextOut(100,150, _T("¼ÒÇÁÆ®¿þ¾îÇÐ°ú"));
	
	CString str;
	str.Format(_T("(%d, %d)"), rect.Width(), rect.Height());
	dc.TextOutW(0,0,str);

	dc.SelectObject(pen2);
	dc.SelectObject(brush2);
	dc.SetBkMode(OPAQUE);
	dc.SetBkColor(RGB(255,255,255));

	CRect text_rect(200,200,400,300);
	dc.Rectangle(text_rect);
	dc.DrawText(_T("draw text text!"), text_rect, 
		DT_CENTER | DT_VCENTER | DT_SINGLELINE);
	
	dc.MoveTo(100,90);
	dc.LineTo(100,110);
	dc.MoveTo(90,100);
	dc.LineTo(110,100);

	// Do not call CWnd::OnPaint() for painting messages
}

