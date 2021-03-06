
// ChildView.h: CChildView 클래스의 인터페이스
//


#pragma once


// CChildView 창

class CChildView : public CWnd
{
// 생성입니다.
public:
	CChildView();
	enum {CIRCLE, MERGE, DIV};


// 특성입니다.
public:
	CList<CRect> m_rect;
	int m_flag;
	int dt, r;
	int m_mergeFlag;
	POSITION m_pos;
	int color;

// 작업입니다.
public:

// 재정의입니다.
	protected:
	virtual BOOL PreCreateWindow(CREATESTRUCT& cs);

// 구현입니다.
public:
	virtual ~CChildView();

	// 생성된 메시지 맵 함수
protected:
	afx_msg void OnPaint();
	DECLARE_MESSAGE_MAP()
public:
	afx_msg void OnLButtonDown(UINT nFlags, CPoint point);
	afx_msg void OnButtonCircle();
	afx_msg void OnButtonDiv();
	afx_msg void OnButtonMerge();
	afx_msg void OnUpdateButtonCircle(CCmdUI *pCmdUI);
	afx_msg void OnUpdateButtonDiv(CCmdUI *pCmdUI);
	afx_msg void OnUpdateButtonMerge(CCmdUI *pCmdUI);
	afx_msg void OnMouseMove(UINT nFlags, CPoint point);
	afx_msg void OnLButtonUp(UINT nFlags, CPoint point);
};