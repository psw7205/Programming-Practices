#include<iostream>
#include<string>
using namespace std;

class Circle
{
private:
	int radius;
	string name;
public:
	void setCircle(string in_name, int in_radius);
	double getArea();
	string getName();
};

class CircleManger
{
private:
	Circle * p;
	int size;
public:
	CircleManger(int in_size);
	~CircleManger();
	void searchByName();
	void searchByArea();
};
void Circle::setCircle(string in_name, int in_radius)
{
	this->name = in_name;
	this->radius = in_radius;
} // 인자로 입력받은 변수들을 멤버변수에 저장합니다.
double Circle::getArea()
{
	return 3.14 * radius * radius; // pi*r^2을 구해 리턴합니다.
}
string Circle::getName()
{
	return name; 
}

CircleManger::CircleManger(int in_size)
{
	string name;
	int r = 0;
	p = new Circle[in_size];
	this->size = in_size;
	for (int i = 0; i < in_size; i++)
	{
		cout << "원 " << i + 1 << "의 이름과 반지름 >> ";
		cin >> name >> r;
		p[i].setCircle(name, r);
	}
} // Circle 배열을 동적할당하고 이름과 반지름을 입력받습니다.
CircleManger::~CircleManger()
{
	delete[] p;
} // 동적할당 받은 Circle 클래스 p 배열을 반환합니다. 
void CircleManger::searchByName()
{
	string name;
	cout << "검색하고자 하는 원의 이름 >> ";
	cin >> name;
	for (int i = 0; i < size; i++)
	{
		if (p[i].getName() == name)
			cout << p[i].getName() << "의 면적은 " << p[i].getArea() << endl;
	}
} // 이름을 입력받고 저장된 이름과 비교한 뒤 같을 경우 출력합니다. 
void CircleManger::searchByArea()
{
	int area = 0;
	cout << "최소 면적을 정수로 입력하세요 >> ";
	cin >> area;
	cout << area << "보다 큰 원을 검색합니다" << endl;

	for (int i = 0; i < size; i++)
	{
		if (p[i].getArea() >= area)
		{
			cout << p[i].getName() << "의 면적은 " << p[i].getArea() << ",";
		}
	}
	cout << endl;
} // 더 면적이 큰 경우를 찾아 출력합니다.

int main()
{
	int n = 0;

	cout << "원의 개수 >> ";
	cin >> n;

	CircleManger c(n);
	c.searchByName();
	c.searchByArea();

	return 0;
}