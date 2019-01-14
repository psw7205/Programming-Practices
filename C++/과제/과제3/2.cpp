#include <iostream>
using namespace std;

class Sample 
{
private: 
	int *p;
	int size;
public:
	Sample(int in_n) // 정수를 사이즈에 저장하고 정수만큼 동적배열을 할당하는 생성자입니다.
	{
		size = in_n; 
		p = new int[in_n]; 
	}

	void read(); // 동적할당 받은 배열 p에 정수 입력받는 함수입니다.
	void write(); // 정수배열을 화면에 출력하는 함수입니다.
	int big(); // 정수배열에서 가장 큰 수 리턴합니다.
	~Sample(); // 동적할당한 p를 해제하기 위한 소멸자입니다.
};

void Sample::read()
{
	for (int i = 0; i < size; i++)
	{
		cin >> p[i]; // size의 갯수만큼 반복하여 입력합니다; 
	}
}

void Sample::write()
{
	for (int i = 0; i < size; i++)
	{
		cout << p[i] << "/"; // 순서대로 출력합니다. 
	}
	cout << endl;
}

int Sample::big()
{
	int temp = p[0];
	for (int i = 0; i < size; i++)
	{
		temp = (temp > p[i]) ? temp : p[i]; 
	}
	return temp; // 가장 큰 값을 리턴합니다.
}

Sample::~Sample()
{
	delete[] p; // 동적할당한 배열 p를 반환합니다.
}

int main()
{
	Sample s(10);
	s.read();
	s.write();
	cout << "가장 큰 수는 " << s.big() << endl;
	return 0;
}
