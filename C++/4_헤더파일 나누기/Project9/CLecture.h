#pragma once

#include "CStudent.h"
#include <string>
using namespace std;

class CLecture
{
public:
	CLecture();
	~CLecture();

	string m_name;
	CStudent * m_pStudents[40]; //포인터 배열

};

