#include "stdafx.h"
#include "CMyShape.h"


CMyShape::CMyShape()
{
	m_color = RGB(rand() % 256, rand() % 256, rand() % 256);
}


CMyShape::~CMyShape()
{
}
