#include <iostream>
using namespace std;
#include <string>

int total_num = 0;

class Student
{
	int num;
	void setNum()
	{
		total_num ++;
		num = total_num;
	}
	
public:
	// constructor 
	Student()					// default constructor
	{
		name = "무명";
		setNum();
		score = 0;
	}
	Student(string in_name)
	{
		name = in_name;
		setNum();
		score = 0;
	}
	Student(string in_name, float in_score)
	{
		name = in_name;
		setNum();
		score = in_score;
	}

	string name;
	float score;

	void print();
	void computeScore(int m, int k, int e)
	{
		score = (m+k+e)/3.0f;
	}
};


void Student::print()
{
	cout<<"--------------------------"<<endl;
	cout<<"이름:"<<name<<endl;
	cout<<"학번:"<<num<<endl;
	cout<<"점수:"<<score<<endl;
	cout<<"--------------------------"<<endl;
}


int main()
{
	Student a("Kim");
	a.computeScore(100,90,90);
	a.print();

	
	Student b("Lee");
	b.computeScore(10,10,20);
	b.print();

	Student c("Park", 50);
	c.print();

	Student d;
	d.print();

	return 0;
}