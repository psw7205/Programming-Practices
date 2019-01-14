#ifndef _STUDENT_H_ // 이 문자가 정의가 안되있으면
#define _STUDENT_H_ // 이 문자를 정의해라 정의 되있다면 건너띄기 = #pragma once : VS전용 다른 ide에선 오류남

#include<string>
using namespace std;

class CStudent
{
private:

	int m_num;
public:
	CStudent();
	~CStudent();
	CStudent(string in_name);
	double m_score;
	string m_name;

private:
	// setting the num
	void setNum();
public:
	void print();
};

#endif
