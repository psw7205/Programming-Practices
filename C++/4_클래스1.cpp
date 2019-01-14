#include<iostream>
#include<string>
#pragma warning(disable: 4996)//vs2017버전 strtok의 c4996 오류를 무시

using namespace std;

/*
struct student
{
	string name;
	int num;
	double score;

}; // 구조체

void printStudent(student in)
{
	cout << "이름:" << in.name << endl;
	cout << "학번:" << in.num << endl;
	cout << "점수:" << in.score << endl;
}

void computeScore(student *in, int m, int k, int e)
{
in->num = (m + k + e) / 3.0f;
}
*/

int total_num = 0;

class student
{
	int num;

	void setnum()
	{
		total_num++;
		num = total_num;
	} // 학번을 사용자가 접근할 수 있으면 매번 호출해야하고 실수(중복 등)가 있을 수 있기에 은닉시킴

public: // 디폴트값은 은닉, public을 이용 밖에서 수정 가능하게 함, num은 수정 불가능 public이하는 수정 가능
	
	string name;
	double score;

	student() // 디폴트 생성자
	{
		name = "무명";
		setnum();
		score = 0;
	}

	student(string in_name) // constructor 생성자, 이 변수가 있어야만 변수생성 가능
	{
		name = in_name;
		setnum();
	} // 선언 할떄 반듯이 name이 있어야 변수선언 가능, 자동으로 학번을 부여(사용자가 컨트롤 X)

	student(string in_name, double in_score) // constructor 생성자, 이 변수가 있어야만 변수생성 가능
	{
		name = in_name;
		setnum();
		score = in_score;
	} // 생성자는 여러개 생성가능 인자에 따라 알아서 호출됨

	void print();

	void computeScore(int m, int k, int e)
	{
		score = (m + k + e) / 3.0f;
	}


}; // 구조체에서 데이터 뿐만아니라 함수까지 종속시킴 
// 작성자의 의도 추가(사용자가 마음대로 못하게) struct -> class


void student::print()
{
	cout << "---------------------------------" << endl;
	cout << "이름:" << name << endl;
	cout << "학번:" << num << endl;
	cout << "점수:" << score << endl;
	cout << "---------------------------------" << endl;
} // clss밖에서 정의 가능



int main()
{
	student a("kim");
	//student a; a.name = "kim"; 불가능 
	//a.num = 10; // class에서 사용자가 수정 불가능하게 막음
	//a.setnum();
	a.computeScore(100, 90, 90); //computeScore(&a, 100, 90, 90); 종속 안시켰을 떈 포인터를 이용해서 함수호출
	a.print();

	student b("park");
	b.computeScore(10, 20, 20);
	b.print();

	student c("Lee", 30);
	c.print();

	student d;
	d.print();

	return 0;
}
