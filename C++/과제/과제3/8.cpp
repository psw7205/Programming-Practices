#include<iostream>
#include<string>
using namespace std;

class Person
{
private:
	string name;
public:
	Person() {	} // 이미 입력변수가 있는 생성자가 있어 기본 생성자를 추가했습니다. 
	Person(string in_name) { this->name = in_name; }
	void setName(string in_name) { this->name = in_name; } // this포인터를 이용해 이름을 Person클래스의 name 변수에 저장했습니다. 
	string getName() { return name; }
};

class Family
{
private:
	Person * p;
	int size;
	string m_name; // Family구성원의 이름을 저장할 변수입니다.
public:
	Family(string in_name, int in_n);
	void show();
	void setName(int in_i, string in_name);
	~Family();
};

Family::Family(string in_name, int in_n)
{
	p = new Person[in_n];
	this->m_name = in_name;
	this->size = in_n;
} // Family name과 몇명인지를 멤버변수에 저장하고 가족 수 만큼 Person 클래스를 동적할당합니다

void Family::show()
{
	cout << m_name << "가족은 다음과 같이 " << size << "명 입니다." << endl;
	for (int i = 0; i < size; i++)
	{
		cout << p[i].getName() << "\t";
	}
} // 저장된 Famliy name과 구성원들을 출력합니다.

void Family::setName(int i, string in_name)
{
	p[i].setName(in_name);
}  // 가족 구성원의 이름을 저장합니다.

Family::~Family()
{
	delete[] p;
} // 동적할당한 Person클래스 배열을 반환합니다.

int main()
{
	Family *simpson = new Family("Simpson", 3);
	simpson->setName(0, "Mr. Simpson");
	simpson->setName(1, "Mrs. Simpson");
	simpson->setName(2, "Bart Simpson");
	simpson->show();
	delete simpson;
}