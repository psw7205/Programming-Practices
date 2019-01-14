#include<iostream>
#include<string>
#include<vector>
#include<list> // vector의 연결리스트 버전
using namespace std;

/*
generic programming (일반적 프로그래밍) = template
함수의 데이터 타입에 종속되지 않게 일반적으로 사용 가능하게 하는 프로그래밍
템플릿이란 방식으로 구현
장점 : 재사용이 편함, 데이터 스트럭쳐 등 특정 분야에서 매우 유용함 
단점 : 읽기 힘듬(가독성이 매우 나빠짐), 디버깅이 어려움

STL - 표준 템플릿 라이브러리
구성
컨테이너 - 템플릿 클래스
iterator - 컨테이너 원소에 대한 포인터
알고리즘 - 템플릿 함수
*/

template <class T> //템플릿 함수, T를 그때그때 바꿔치기함
T bigger(T a, T b)
{
	if (a > b)
		return a;
	return b;
}

template <class T, class S> // 심볼 여러개 설정 가능 
S div(T a, T b)
{
	S out;
	out = (S)a / (S)b;
	return out;
}

template <class T>
void mySwap(T &a, T &b)
{
	T temp = a;
	a = b;
	b = temp;
}

// class말고 typename도 가능 
template<typename T>  // 템플릿 클래스
class SmartArr
{
	T *data;
	int size;
public:
	SmartArr(int n)
	{
		size = n;
		data = new T[n];
	}

	~SmartArr() { delete[] data; }

	T & operator[](int ind){ return data[ind];	}

	int getsize() { return size; }
};

int main()
{
	cout << bigger<int>(3, 4) << endl;
	cout << bigger<double>(3.3, 4.2) << endl;
	cout << bigger<char>('a', 'b') << endl; // 인자가 명확한경우 <>를 생략해도 가능

	cout << div<int, double>(3, 4) << endl;

	int a = 10; 
	int b = 20;

	mySwap(a, b);
	cout << a << endl;

	string c = "abc";
	string d = "def";

	mySwap(c, d);
	cout << c << endl;

	SmartArr<int> arr(10);
	
	for (int i = 0; i < arr.getsize(); i++)
		arr[i] = i * 2;
	for (int i = 0; i < arr.getsize(); i++)
		cout << arr[i] << endl;

	vector<string> arr2(10); // SmartArr와 같은 내용의 이미 만들어져있는 템플릿 클래스
	for (int i = 0; i < arr2.size(); i++)
		arr2[i] = "aaa";
	for (int i = 0; i < arr2.size(); i++)
		cout << arr2[i] << endl;

	vector<int> arr3;
	for (int i = 0; i < 10; i++)
		arr3.push_back(i); // 뒤에 추가하는 함수 - 이미 구현되어있음. 그냥 인터넷에서 찾아보고 쓰면 됨

	arr3.resize(20, 100); // 사이즈를 20 빈 곳을 100으로 초기화 

	for (int i = 0; i < arr3.size(); i++)
		cout << arr3[i] << endl;


	list<int> arr4; //연결리스트이기 때문에 검색히려면 순회해야함
	for (int i = 0; i < 10; i++)
		arr4.push_back(i);

	list<int>::iterator it; // int형식의 list를 가르키는 이터레이터 it

	it = arr4.begin(); // 시작 노드를 가르킴

	while (it != arr4.end()) // 끝이 아닐때까지
	{
		cout << (*it) << endl; // 포인터 주소가 가르키는 값
		it++; // 다음으로 넘어감 it = it -> next;
	}

	it = arr4.begin(); // 처음을 가르키고
	it++;
	it++;
	it++; // 3번째 칸으로 이동시키고

	arr4.erase(it); // 삭제함

	arr4.sort();// 정렬
	arr4.unique(); // 한개만 출력 


	return 0;
}