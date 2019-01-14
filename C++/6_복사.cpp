#include<iostream>
using namespace std;

class CMyArray
{
private:
	CMyArray(CMyArray & in) {}; //private에 놓는다면 복사가 금지됨
	int m_size;
	int* m_pData;
public:
	CMyArray(int size)
	{
		m_size = size;
		m_pData = new int[size]; // 클래스는 8바이트만 동적할당된 메모리는 클래스 밖(힙)에 저장됨
	}

	CMyArray(CMyArray & in) // copy constructor 
	{
		m_size = in.m_size;
		m_pData = new int[m_size];
		for (int i = 0; i < m_size; i++)
			m_pData[i] = in.m_pData[i];
	} // 복사 생성자 (깊은 복사) : 직접 안만들어 준다면 기본 복사 생성자가 만들어지고 얕은 복사로 수행됨

	~CMyArray() { delete[] m_pData; }
	int getSize() { return m_size; }
	/*
	int getAt(int ind) { return m_pData[ind]; }
	void setAt(int ind, int value) { m_pData[ind] = value; }
	*/
	int & at(int ind) { return m_pData[ind]; } // 리턴값 참조로 위 두개 함수 통합 가능 (값이 함수가 끝난 후 사라진다면 당연히 안됨)

	int & operator [] (int ind) { return m_pData[ind]; }

	CMyArray & operator = (CMyArray & in)
	{
		delete[] m_pData;
		m_size = in.m_size;
		m_pData = new int[m_size];
		for (int i = 0; i < m_size; i++)
			m_pData[i] = in.m_pData[i];
		return *this;
	} // 할당 

};

/*
int sumi(int a, int b) { return a + b; }
double sumd(double a, double b) { return a + b; } 
C언어에선 인자에 따라 다른 자료형의 서로 다른 이름의 함수들이 필요함 
C++에선 같은 이름의 함수를 인자만 다르게 중복 가능
*/

int sum(int a, int b) { return a + b; }
double sum(double a, double b) { return a + b; }
float sum(float a, float b) { return a + b; }

int main()
{
	cout << sum(10, 20) << endl;
	cout << sum(10.5, 20.8) << endl;

	CMyArray arr(10);

	/*
	for (int i = 0; i < arr.getSize(); i++)
		arr.setAt(i, i * 2);
	for (int i = 0; i < arr.getSize(); i++)
		cout << i << " : " << arr.getAt(i) << endl;
	*/

	for (int i = 0; i < arr.getSize(); i++)
		// arr.at(i) = i * 2 ;
		arr[i] = i * 2; // operater []이 보이면 m_pData[ind]를 리턴 
	for (int i = 0; i < arr.getSize(); i++)
		cout << i << " : " << arr[i] << endl;// arr.at(i) << endl;

	CMyArray brr = arr;
	/*
	copy constructor, copy 하게 되면 int m_size와 int * m_pData를 복사함
	포인터 주소도 복사하기 때문에 b를 바꿔도 a가 바뀜, b와 a 모두 한 데이터를 가리킴
	얕은 복사(shallow copy) 보이는 것만 복사함
	-----------------------------------------------
	CMyArray brr;
	brr = arr; // assignment (할당)
	복사와 할당은 다르다...
	*/

	CMyArray crr(arr); // == CMyArray crr = arr; 

	for (int i = 0; i < arr.getSize(); i++)
		brr[i] = i * 3; 
	for (int i = 0; i < arr.getSize(); i++)
		cout << i << " : " << brr[i] << endl;

	for (int i = 0; i < arr.getSize(); i++)
		cout << i << " : " << arr[i] << endl; // b값을 바꿨음에도 a값도 같이 바뀜 모두 한 데이터를 가리키기 때문...

	return 0;
}