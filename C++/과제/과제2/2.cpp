#include<iostream>
#include<string>
using namespace std;

class Date
{
private:
	int m_y = 0, m_m = 0, m_d = 0;
public:
	Date(int Year, int Month, int day);
	Date(string d);
	void show();
	int getYear();
	int getMonth();
	int getDay();
};

Date::Date(int Year, int Month, int Day)
{
	m_y = Year;
	m_m = Month;
	m_d = Day;
}

Date::Date(string d)
{
	int s = 0, s2 = 0;
	
	s = d.find('/');
	s2 = d.find_last_of('/');

	m_y = stoi(d.substr(0, s));
	m_m = stoi(d.substr(s+1, s2-s-1));
	m_d = stoi(d.substr(s2+1, d.length()));
}

void Date::show()
{
	cout << m_y << "³â" << m_m << "¿ù" << m_d << "ÀÏ" << endl;
}

int Date::getYear()
{
	return m_y;
}
int Date::getMonth()
{
	return m_m;
}
int Date::getDay()
{
	return m_d;
}

int main()
{

	Date birth(2014, 3, 20);
	Date independenceDay("1945/8/15");
	independenceDay.show();
	cout << birth.getYear() << ',' << birth.getMonth() << ',' << birth.getDay() << endl;

	return 0;
}