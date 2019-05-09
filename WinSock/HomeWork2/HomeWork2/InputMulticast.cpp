// InputMulticast.cpp: 구현 파일
//

#include "stdafx.h"
#include "HomeWork2.h"
#include "InputMulticast.h"
#include "afxdialogex.h"


// InputMulticast 대화 상자

IMPLEMENT_DYNAMIC(InputMulticast, CDialogEx)

InputMulticast::InputMulticast(CWnd* pParent /*=nullptr*/)
	: CDialogEx(IDD_DIALOG1, pParent)
	, name(_T(""))
	, ipAddr(0)
{

}

InputMulticast::~InputMulticast()
{
}

void InputMulticast::DoDataExchange(CDataExchange* pDX)
{
	CDialogEx::DoDataExchange(pDX);
	DDX_Text(pDX, IDC_EDIT2, name);
	DDX_IPAddress(pDX, IDC_IPADDRESS1, ipAddr);
	DDV_MinMaxUInt(pDX, ipAddr, 0, 255);
	DDX_Control(pDX, IDC_EDIT1, port);
}


BEGIN_MESSAGE_MAP(InputMulticast, CDialogEx)
	ON_BN_CLICKED(IDC_BUTTON1, &InputMulticast::OnBnClickedButton1)
	ON_EN_UPDATE(IDC_EDIT1, &InputMulticast::OnEnUpdateEdit1)
END_MESSAGE_MAP()


// InputMulticast 메시지 처리기


void InputMulticast::OnBnClickedButton1()
{
	bool isMultiCast = true;
	bool isTruePort = true;

	if (isMultiCast && isTruePort)
	{
		this->OnClose();
	}
	else
	{
		
	}
}


void InputMulticast::OnCancel()
{
	// TODO: 여기에 특수화된 코드를 추가 및/또는 기본 클래스를 호출합니다.
	mainDlg->isClose = true;
	CDialogEx::OnCancel();
}


void InputMulticast::OnEnUpdateEdit1()
{
	CString str;
	port.GetWindowTextA(str);
}
