#include<iostream>
using namespace std;

class CShape
{
public:
	int x, y;
	
	CShape()
	{
		x = 0;
		y = 0;
	}

	CShape(int _x, int _y)
	{
		x = _x;
		y = _y;
	}
	virtual ~CShape() {} // 주소에 존재하는 진짜 데이터에 맞는 소멸자를 실행함

	virtual void draw() // virtual, 주소에 존재하는 진짜 함수를 수행한다. 동적 바인딩 지시어
	{
		cout << "Shape:(" << x << "," << y << ")" << endl;
	}

};

class CRect: public CShape  
{// 보통 부모클래스는 내가 만든 것이 아니고 어떤 방식으로 돌아가는 지 모르기 때문에 항상 직접 만든 클래쓰의 변수만 건드린다.
public:
	int w, h;
	CRect() // : CShpae() , 안써주면 부모클래스의 디폴트 생성자가 자동으로 삽입됨
	{
		w = 1;
		h = 1;
	}

	CRect(int _x, int _y, int _w, int _h)
		: CShape(_x, _y)
	{
		w = _w;
		h = _h;
	}

	void draw() // overriding 부모 클래스의 함수를 자기가 수정, 추가해서 사용 가능.
	{
		// CShape::draw(); // 부모클래스 CShape의 draw()함수를 먼저 실행하고 추가적으로 다른 코드를 수행함
		cout<<"Rect:(" << x << "," << y << ") " << w<< "," << h <<  endl;
	}

};

class CCircle : public CShape
{
public:
	int r;
	CCircle()
	{
		r = 1;
	}
	CCircle(int _x, int _y, int _r)
		:CShape(_x, _y)
	{
		r = _r;
	}
	
	void draw()
	{
		cout << "Circle:(" << x << "," << y << ") " << r << endl;
	}
};

void func(CShape *o)
{
	o->x += 10;
	o->y += 10;
}

int main()
{
	CShape a;
	CRect b;
	CRect c(1, 2, 3, 4);

	CShape d = c; // 서로 다른 클래스(자식->부모)지만 복사 가능 : 상향형변환 up casting
	// CRect e = a; 부모 -> 자식은 불가능 : 하향형변환 X down casting(w, h를 초기화 할 방법이 모호하기 때문에...)

	CShape *p1 = &c; // 포인터의 상향형변환은 언제나 가능
	p1->draw(); // c는 CRect클래스지만 p1이 CShape의 변수만 사용하므로 CShape::draw()로 실행됨

	// CRect *p2 = &a; // 포인터의 하향형변환은 특정 조건일 때만 가능 
	CRect *p2 = (CRect*) p1; // CShape 포인터지만 주소가 가르키는 c는 CRect이므로 강제형변환으로 사용 가능
	p2->draw();

	a.draw();
	b.draw();
	c.draw();
	d.draw(); 

	CShape *p[3]; // 하나의 배열에 서로 다른 클래스를 하나로 묶어서 관리 가능
	p[0] = new CShape (20, 10);
	p[1] = new CRect(1, 2, 3, 4);
	p[2] = new CCircle (10, 20, 100);

	CRect *r = (CRect*)p[1];
	r->w = 10; 

	func(p[2]);

	for (int i = 0; i < 3; i++)
		p[i]->draw(); // virtual선언을 했기에 불리는 시점에 진짜 데이터를 확인하고 수행 , 동적 바인딩 : 다형성 (polymorphism)

	for (int i = 0; i < 3; i++)
		delete p[i]; 
	
	return 0;
}