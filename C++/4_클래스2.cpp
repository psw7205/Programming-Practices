#include<iostream>
using namespace std;
#include<string>

int total_num = 0;

class student
{
private: // 안 쓰면 자동적으로 퍼블릭 위가 프라이빗으로 설정됨
	int num;


	void setnum()
	{
		total_num++;
		num = total_num;
		
	} 

public:
	student();
	student(string in_name);
	student(string in_name, double in_score);

	~student()
	{
		cout << name << " is distructed" << endl;
	}	// 소멸자 : 오직 한번만 자동호출, 변수의 소멸 시기 확인 가능, 동적 메모리 삭제 기능 ... 
		//c언어는 작성자가 메모리를 직접 관리해줘야함, 소멸시키지 않는다면 데이터가 누적되어 메모리 누수가 생김

	string	name;
	double score;


	void print()
	{
		cout << " name : " << name << endl;
		cout << " num : " << num << endl;
		cout << " score : " << score << endl;
	}

};

student::student()
{
	name = "none";
	setnum();
	score = 0;
	cout << name << " is created" << endl;
} // default constructor 색기본 생성자 

student::student(string in_name)
{
	name = in_name;
	setnum();
	score = 0;
	cout << name << " is created" << endl;
}// 생성자 : 반듯이 한번, 맨처음 호출시킴, 변수의 초기화 가능

student::student(string in_name, double in_score)
{
	name = in_name;
	setnum();
	score = in_score;
	cout << name << " is created" << endl;
}// 서로 다른 생성자 설정 가능

student g("global");
void func()
{
	student l("local");
}

class smartarray
{
	int size;
	int *data;
public:
	smartarray(int s)
	{
		size = s;
		data = (int*)malloc(sizeof(int)*size);
	}
	smartarray()
	{
		free(data);
	}
	int & operator [] (int ind)
	{
		return data[ind];
	} // [ind]를 보면 data[ind]로 바꿈 

};



int main()
{
	student a("Lee"), b("park"), c;

	{
		student ll("lol");
	} // 중괄호가 끝나면 변수가 끝남, 소멸자로 확인 가능

	a.score = 100;

	a.print();
	b.print();
	c.print();

	func();

	/*
	int *data = (int *)malloc(sizeof(int) * 100);
	data[0] = 1;

	free(data); // 사용이 끝났으면 소멸시켜야 데이터 누수가 안생김
	동적 할당 구조 */

	smartarray arr(100);
	//arr.data[10] = 1;
	arr[10] = 1; //operator로 사용 가능 

	cout << arr[10] << endl;

	return 0;
}