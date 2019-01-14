#include <iostream>
#include <string>
using namespace std;

class CShape // 부모 클래스
{
private:
protected:
	double x, y;
	string color;
public:
	CShape()
	{
		x = 0;
		y = 0;
		color = "black";
	}

	CShape(double _x, double _y, string c)
	{
		x = _x;
		y = _y;
		color = c;
	}

	void print()
	{
		cout << x << "," << y << " - " << color << endl;
	}
};

class CRect : public CShape // CRect 클래스는 CShape 클래스를 상속받음, private는 접근 불가 protected 까지 접근 가능
{
private :
	double width, height;
public:

	CRect() {};

	CRect(double w, double h)
	{
		width = w;
		height = h;
	}

	CRect(double x, double y, string c, double w, double h)
		: CShape(x, y, c) // 부모클래스의 생성자를 골라서 호출할 때 사용, 없다면 디폴트생성자가 호출됨
	{
		width = w;
		height = h;
	}
	void printRect()
	{
		cout << x << "," << y << " - " << color;
		cout << " - " << width << "," << height << endl;
	}

	void print() // 같은 이름의 함수로 덮어 쓰기 가능, 함수오버라이딩
	{
		cout << x << "," << y << " - " << color;
		cout << " - " << width << "," << height << endl;
	}
};

/*
class a
class b : a
class c : b
생성자는 a - b - c 순서로 호출되고
소멸자는 c - b - a 순서로 호출된다.
*/

int main()
{
	CShape a;
	a.print();

	CRect b;
	b.printRect(); // 부모클래스의 기본생성자가 호출되서 x, y가 0으로 초기화된다. b의 기본 생성자가 없기 때문에 width와 height는 쓰레기 값이 저장되어있다.

	CRect c(15, 20);
	c.print(); // CShape에도 print()가 있지만 CRect 클래스에 있는 print()가 호출됨 , 함수 오버라이딩, 같은 이름의 함수여도 클래스에 따라 다르게 호출 가능

	CRect d(10, 20, "red", 100, 100);
	d.print();

	return 0;
}