#include<iostream>
#include<cstdlib>
#include<ctime>
using namespace std;

class Random
{
private:
	int m_r = 0;
public:
	Random();
	int next();
	int nextInRange(int a, int b);
};

Random::Random()
{
	srand((unsigned)time(0));
}

int Random::next()
{
	m_r = rand();
	return m_r;
}

int Random::nextInRange(int a, int b)
{
	m_r = rand()%(b + 1 - a) + a ;
	return m_r;
}

int main()
{
	Random r;
	cout << "-- 0에서 " << RAND_MAX << "까지의 랜덤 정수 10개 --" << endl;
	for (int i = 0; i < 10; i++)
	{
		int n = r.next();
		cout << n << ' ';
	}
	cout << endl << endl << "-- 2에서 " << "4까지의 랜덤정수 10개 --" << endl;
	for (int i = 0; i < 10 ; i++)
	{ 
		int n = r.nextInRange(2, 4);
		cout << n << ' ';
	}

	cout << endl;

	return 0;
}