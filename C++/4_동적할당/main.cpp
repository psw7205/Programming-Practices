#include <iostream>
using namespace std;

#include "Student.h"
#include "Lecture.h"

CLecture g_cpp; // heap

void func()  // stack , 메모리가 작음 큰 변수 선언은 heap(함수 밖)에서 선언
{
	// func(); : 종료없는 재귀함수를 쓰면 stack overflow가 생김
	//int temp[1000][1000]; 실행불가 메모리 부족

	/*
	int * temp = (int *)malloc(sizeof(int) * 1000000); 
	free(temp); c언어 동적 할당 문법 


	int * temp = new int[1000000];
	delete [] temp; // 배열을 지울 때 [] 필수

	int * temp2 = new int;
	delete temp2; c++ 동적할당 문법
	*/

	CStudent * s = new CStudent[2];
	s[0].m_name = "Park";
	s[1].m_name = "Choi";

	CStudent * p1 = new CStudent("Kim");

	CStudent a("Kim");
	CStudent b("Lee");

	g_cpp.m_pStudents[0] = &s[0];
	g_cpp.m_pStudents[1] = &s[1];
	g_cpp.m_pStudents[2] = p1;

}

//void func2(CStudent s[]) = void func2(CStudent *s)
//void func2(CStudent *s[]) = void func2(CStudent **s)
void func2(CStudent **s)
{
	s[0]->m_score = 100;
	s[1]->m_score = 200;
}

void func3(CStudent s[][40]) // 최소단위 설정은 필수
{
	s[0][0];
	s[0][1];
}

void func4(CStudent **t) // void func4(CStudent [][40]) 은 안됨
{
	t[0][0].m_name = "kim";
	t[2][4].m_score = 40;

}

int main()
{
	int  temp[20][40];
	/*
	temp[0][0] = temp [0]
	temp[0][1] = temp [1]
	...
	temp[0][39]
	temp[1][0] = temp[40][0]
	
	temp[i][j] = temp[40*i + j]
	*/

	CStudent s[2][40];
	
	/*
	CStudent * s1 = new CStudent[40];
	CStudent * s2 = new CStudent[60];
	CStudent * s3 = new CStudent[10];

	
	CStudent **t = new CStudent * [3];
	t[0] = new CStudent[40];
	t[1] = new CStudent[60];
	t[2] = new CStudent[10];
	*/

	int n = 10, m = 40;
	CStudent **t = new CStudent *[n];
	for (int i = 0; i < n; i++)
		t[i] = new CStudent[m];

	func4(t);

	for (int i = 0; i < n; i++)
		delete[] t[i];
	delete[] t;


	func();
	func2(g_cpp.m_pStudents);


	g_cpp.m_pStudents[0]->print();
	g_cpp.m_pStudents[1]->print();
	g_cpp.m_pStudents[2]->print();

	delete [] g_cpp.m_pStudents[0];
	g_cpp.m_pStudents[0] = NULL;
	g_cpp.m_pStudents[1] = NULL;

	delete g_cpp.m_pStudents[2];
	g_cpp.m_pStudents[2] = NULL; // 지운 후 지운 주소는 NULL로 초기화 필수

	return 0;
}