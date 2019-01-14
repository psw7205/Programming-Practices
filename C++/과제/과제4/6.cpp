#include<iostream>
using namespace std;

class MyIntStack 
{
	int *p; // 스택메모리로 사용할 포인터
	int size; // 스택의 최대 크기
	int tos; // 스택의 탑을 가르키는 인덱스
public:
	MyIntStack();
	MyIntStack(int size);
	MyIntStack(MyIntStack& s);// 복사 생성자
	~MyIntStack();

	bool push(int n); // 정수 n을 푸쉬, 꽉차있으면 false 아니면 true리턴
	bool pop(int &n); // 스택 탑에 있는 값을 n에 팝, 비어있으면 false 아니면 true 리턴
};

MyIntStack::MyIntStack(int size)
{
	tos = 0; // 스택의 tos는 0부터 시작합니다. 
	p = new int[size]; // size의 크기만큼 동적할당합니다.
	this->size = size; // size를 멤버변수 size에 저장합니다. 
}
 
MyIntStack::~MyIntStack()
{
	delete[] p;
} // 클래스가 끝나면 동적할당한 p[]을 반환합니다.

bool MyIntStack::push(int n)
{
	if(tos == size) // 최고 위치가 size와 같으면 스택이 꽉 찬것이므로 false를 리턴합니다.
		return false;
	else
	{
		p[tos] = n; // n을 스택에 저장합니다.
		tos++; // 최고위치가 0부터 시작했으므로 값을 넣고 1증가시킵니다.
		return true;
	}
}

MyIntStack::MyIntStack(MyIntStack& s)
{
	size = s.size;
	tos = s.tos;
	p = new int[size]; //깊은 복사를 위해 새롭게 동적할당합니다.
	for(int i = 0 ; i < size; i++)
		p[i] = s.p[i]; // 깊은 복사를 위해 데이터 까지 복사합니다.
}

bool MyIntStack::pop(int &n)
{
	if(tos == 0) // 최고위치가 0이면 스택이 비어있는 것이므로 0을 출력합니다.
		return false;
	else
	{
		tos--;// push에서 데이터를 넣고 증가시켰기 때문에 마지막 tos는 최고위치보다 1 큽니다. 그러므로 먼저 감소시키고 데이터를 저장합니다.
		n = p[tos]; // 참조를 이용해 n에 데이터를 저장합니다.
		return true;
	}
}


int main()
{
	MyIntStack a(10); // 스택의 크기가 10인 a를 생성합니다.
	a.push(10); // 10을 push합니다
	a.push(20); // 20을 push합니다

	MyIntStack b = a; // b를 만들고 a를 깊은 복사합니다.
	b.push(30); // b에 30을 넣습니다.

	int n ;

	a.pop(n); // a에서 pop합니다.
	cout << "스택 a에서 팝한 값 " << n << endl;
	b.pop(n); // b에서 pop합니다.
	cout << "스택 b에서 팝한 값 " << n << endl;

	return 0;
}
