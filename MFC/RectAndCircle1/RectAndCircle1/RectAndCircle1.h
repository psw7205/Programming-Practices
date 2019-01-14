
// RectAndCircle1.h : main header file for the RectAndCircle1 application
//
#pragma once

#ifndef __AFXWIN_H__
	#error "include 'stdafx.h' before including this file for PCH"
#endif

#include "resource.h"       // main symbols


// CRectAndCircle1App:
// See RectAndCircle1.cpp for the implementation of this class
//

class CRectAndCircle1App : public CWinAppEx
{
public:
	CRectAndCircle1App();


// Overrides
public:
	virtual BOOL InitInstance();
	virtual int ExitInstance();

// Implementation

public:
	UINT  m_nAppLook;
	BOOL  m_bHiColorIcons;

	virtual void PreLoadState();
	virtual void LoadCustomState();
	virtual void SaveCustomState();

	afx_msg void OnAppAbout();
	DECLARE_MESSAGE_MAP()
};

extern CRectAndCircle1App theApp;
