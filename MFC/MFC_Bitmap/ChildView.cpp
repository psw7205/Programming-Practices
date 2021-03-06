
// ChildView.cpp: CChildView 클래스의 구현
//

#include "stdafx.h"
#include "Bitmap.h"
#include "ChildView.h"

#ifdef _DEBUG
#define new DEBUG_NEW
#endif


// CChildView

CChildView::CChildView()
{
	m_x = 0;
	m_y = 0;
}

CChildView::~CChildView()
{
}


BEGIN_MESSAGE_MAP(CChildView, CWnd)
	ON_WM_PAINT()
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

	CBitmap bmp;
	bmp.LoadBitmapW(IDB_BITMAP1);

	BITMAP bmpInfo; // 비트맵의 정보를 알 수 있는 구조체
	bmp.GetBitmap(&bmpInfo); // bmp의 내용을 bmpinfo에 저장

	CRect rect;
	GetClientRect(&rect);

	CDC memDC;
	memDC.CreateCompatibleDC(&dc);
	memDC.SelectObject(&bmp); // 비트맵을 화면과 같은 양식으로 바꿈

	dc.BitBlt(100, 100, bmpInfo.bmWidth, bmpInfo.bmHeight, &memDC, 0, 0, SRCCOPY); // 화면 100,100에 그림 크기만큼 memDC의 0,0부터 그대로 짤라 붙임
	//dc.StretchBlt(0, 0, rect.Width(), rect.Height(), &memDC, 0, 0, bmpInfo.bmWidth, bmpInfo.bmHeight, SRCCOPY); // 화면 전체에 그림을 전부 그림
	
	/*
	for (int x = 0; x < 256; x++)
		for (int y = 0; y < 256; y++)
			dc.SetPixelV(x, y, RGB(x, 0, y)); // 지금은 화면이 수정되면 뚝뚝 끊김
	//화면에 그려지는 또다른 메모리를 만들어서 거기에 그리고 다 그려지면 그 때 화면에 출력하는 방법으로 뚝뚝 끊기는걸 방지함

	
	CBrush brush(&bmp);
	dc.SelectObject(brush); // 브러쉬에 비트맵을 설정하고 그림

	dc.Rectangle(0, 0, bmpInfo.bmWidth, bmpInfo.bmHeight);

	CString str;
	str.Format(_T("bmp : (%d %d)"), bmpInfo.bmWidth, bmpInfo.bmHeight);

	dc.TextOutW(0,0,str);

	CRect rect;
	GetClientRect(&rect);
	dc.Rectangle(0, 0, rect.Width(), rect.Height()); // 화면 크기만큼 여러번 채움
	*/

	dc.Rectangle(m_x, m_y, m_x + 100, m_y + 100);

}


void CChildView::OnLButtonDown(UINT nFlags, CPoint point) // 직접 지울땐 위에 매세지맵과 헤더파일의 선언까지 지워줘야함
{
	m_x = point.x;
	m_y = point.y;

	Invalidate(); // 클릭하면 다시 그리라고 메세지를 보내는 함수

	CWnd::OnLButtonDown(nFlags, point);
}
