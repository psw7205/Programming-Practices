#pragma once
#include "HomeWork2Dlg.h"

// InputMulticast 대화 상자

class InputMulticast : public CDialogEx
{
	DECLARE_DYNAMIC(InputMulticast)

public:
	InputMulticast(CWnd* pParent = nullptr);   // 표준 생성자입니다.
	virtual ~InputMulticast();
	 


// 대화 상자 데이터입니다.
#ifdef AFX_DESIGN_TIME
	enum { IDD = IDD_DIALOG1 };
#endif

protected:
	virtual void DoDataExchange(CDataExchange* pDX);    // DDX/DDV 지원입니다.

	DECLARE_MESSAGE_MAP()
public:
	afx_msg void OnBnClickedButton1();

	CHomeWork2Dlg *mainDlg;

	int result;
	virtual void OnCancel();
	CString name;
	DWORD ipAddr;
	CEdit port;
	afx_msg void OnEnUpdateEdit1();
};
