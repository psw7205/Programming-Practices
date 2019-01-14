#include<iostream>
#include<string>

using namespace std;

class CMyClass
{
public:
	int x, y;
	CMyClass() { x = 1; y = 2; }
	CMyClass(int _x, int _y) { x = _x; y = _y; }
	//== CMyClass(int _x = 1, int _y = 2) { x = _x; y = _y; } // 두개 하나로 통합 가능
};

// 중복이 모호하면 에러남 항상 뭐가 뭔지 명확하게 코딩

void func(int w, int h = 3, char c = '*') // c는 안주면 *로 찍고 변수를 주면 그걸로 찍음 (디폴트 매개변수)
{										  // 디폴트 매개변수는 끝에 몰려있어야함, 필수인 변수들은 앞으로
	for (int j = 0; j < h; j++)			  // 클래스 생성자에서도 사용 가능
	{
		for (int i = 0; i < w; i++)
			cout << c;
		cout << endl;
	}
}

int main()
{
	func(3);
	func(3, 5, '&');
	func(3, 5);
	
	CMyClass a;

	
	return 0;
}

