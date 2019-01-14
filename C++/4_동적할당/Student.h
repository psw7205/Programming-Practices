#ifndef _STUDENT_H_ 
#define _STUDENT_H_ 

#include <string>
using namespace std;

class CStudent
{
private:

	int m_num;

public:
	CStudent(void);
	CStudent(string in_name);
	~CStudent(void);

	//hungarian notation
	float m_score;
	string m_name;
private:
	// Setting the num value automatically
	void setNum(void);
public:
	void print(void);
};

#endif