#include "CStudent.h"

#include<iostream>
using namespace std;

int g_totalNum = 0;

CStudent::CStudent()
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


CStudent::~CStudent()
{
}


// setting the num
void CStudent::setNum()
{
	g_totalNum++;
	m_num = g_totalNum;
}


void CStudent::print()
{
	cout << " name : " << m_name << endl;
	cout << " num : " << m_num << endl;
	cout << " score : " << m_score << endl;
}
