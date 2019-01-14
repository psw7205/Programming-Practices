#pragma once

#include "Student.h"
#include <string>
using namespace std;

class CLecture
{
public:
	CLecture(void);
	~CLecture(void);

	string m_name;
	CStudent * m_pStudents[40];
};



