#include "Student.h"
#include <iostream>
using namespace std;


CStudent::CStudent(void)
{
	m_name = "¹«¸í";
	setNum();
	m_score = 0;
}
CStudent::CStudent(string in_name)
{
	m_name = in_name;
	setNum();
	m_score = 0;
}


CStudent::~CStudent(void)
{
}

int g_totalNum = 0;
// Setting the num value automatically
void CStudent::setNum(void)
{
	g_totalNum ++;
	m_num = g_totalNum;
}

void CStudent::print(void)
{
	cout<<"Name: "<<m_name<<endl;
	cout<<"Num: "<<m_num<<endl;
	cout<<"Score: "<<m_score<<endl;
}
