//operator overload 연산자 중복

#include<iostream>
using namespace std;

class CComplex
{
private:
	double real, img;
public:
	CComplex()
	{
		real = 0;
		img = 0;
	}

	CComplex(double a, double b)
	{
		real = a;
		img = b;
	}

	void print()
	{
		cout << "(" << real << "+" << img << "i)" << endl;
	}
	/* 1
	CComplex add(CComplex in)
	{
		CComplex out;
		out.real = real + in.real;
		out.img = img + in.img;
		return out;
	}
	*/
	/* 2
	static CComplex add(CComplex l, CComplex r)
	{
		CComplex out;
		out.real = l.real + r.real;
		out.img = l.img + r.img;
		return out;
	} // 전역으로 선언
	*/
	/* 3
	friend CComplex add(CComplex l, CComplex r); // friend로 지정 하면 스태틱으로 했을 때 처럼 CComplex::를 안써도 됨
	*/
	/* 4
	CComplex operator+( CComplex r)
	{
		CComplex out;
		out.real = real + r.real;
		out.img = img + r.img;
		return out;
	}
	*/	

	CComplex &operator= (const CComplex & r) // const로 참조를 받으면 사용만 하고 참조 받은 값 수정이 불가능함
	{
		real = r.real;
		img = r.img;
		return *this; // 할당을 수행하고 자기자신을 리턴
	} // 할당(=) 연산은 멤버함수로만 가능 

	double & operator[] (int ind)
	{
		//if(ind < 0 || ind >= 2) // 예외처리필요... ,참조 리턴이기에 다른 방법이 없음
		if (ind == 0) return real;
		if (ind == 1) return img;
	}

	friend CComplex operator+(CComplex l, CComplex r);
	friend CComplex operator*(CComplex l, CComplex r);
	friend CComplex operator!(CComplex r);
	friend CComplex operator*(double a, CComplex r);
	friend ostream & operator<<(ostream & stram, const CComplex in);

	// 참조로 받는게 좋음
};
/* 3
CComplex add(CComplex l, CComplex r)
{
	CComplex out;
	out.real = l.real + r.real;
	out.img = l.img + r.img;
	return out;
}
*/
CComplex operator+(CComplex l, CComplex r)
{
	CComplex out;
	out.real = l.real + r.real;
	out.img = l.img + r.img;
	return out;
} // 클래스 안에 멤버 함수로 선언하면 인자는 하나만 받을 수 있고 다른 하나는 멤버변수 본인이 됨

CComplex operator*(CComplex l, CComplex r)
{
	CComplex out;
	out.real = l.real * r.real - l.img * r.img;
	out.img = l.real * r.img  + l.img * r.real;
	return out;
}
CComplex operator*(double a, CComplex r)
{
	CComplex out;
	out.real = a * r.real;
	out.img = a* r.img;
	return out;
}

CComplex operator!(CComplex r)
{
	CComplex out;
	out.real = r.real;
	out.img = - r.img;
	return out;
}

ostream & operator<<(ostream & stream, const CComplex in)
{
	stream<< "(" << in.real << "+" << in.img << "i)" << endl;
	return stream;
}

int main()
{
	CComplex a(3, 4), b(2, 7);
	
	/* 1
	CComplex c = a.add(b); // = b.add(a) // c = a + b
	a.add(b); // a = a + b ... ? 함수로 만들 시 의미가 혼동되기 시작함 
	*/

	/* 2
	CComplex c = CComplex::add(a, b); // CComplex:: 슬 쓰기 귀찮...
	*/
	/* 3
	CComplex c = add(a, b);
	*/
	CComplex c = a + b; // operator+(a, b) == a.operator(b)
	CComplex d = a * b; // 연산자의 재정의가 필요함
	CComplex e = a * (!a);
	CComplex f = 3 * a;
	CComplex g;
	g = 2 * a + 3 * b; // 할당 

	a.print();
	b.print();
	c.print();
	d.print();
	e.print();
	f.print();
	g.print();

	cout << a[0] << "+" << a[1] << endl;

	for (int i = 0; i < 2; i++)
		b[i] = a[i]; // 복사...

	cout << a; //  <<(cout, a) // operator<< 재정의로 a.print()를 대신함
	cout << a << b; //  <<(<<(cout, a),b)

	return 0;
}