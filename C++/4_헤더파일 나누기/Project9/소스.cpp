#include <iostream>
using namespace std;

#include "CStudent.h"
#include "CLecture.h"

int main()
{
	CStudent a("kim");
	a.print();

	CStudent b("Lee");
	b.print();

	/*
	CStudent *p; // 초기화 안하고 포인터를 선언하는건 안좋은 습관
	p = &a; 
	(*p).print();
	*/

	CStudent *p = &b; // 포인터는 그냥 존재하기만 해선 아무 의미 없음 항상 선언과 동시에 초기화 해야 실수방지, 필수
	(*p).print();  // 하나의 변수가 여러 데이터를 바꿔치며 사용가능 
	p->print(); //20번 21번 같은 문장 

	CLecture cpp;
	cpp.m_pStudents[0] = &a;
	cpp.m_pStudents[1] = &b;

	CLecture mp;
	mp.m_pStudents[0] = &a; 

	a.m_name = "park"; // 포인터로 접근하면 데이터를 바꿀때 전부 바꿀 필요 없음
	cpp.m_pStudents[0]->print();
	

	return 0;
}