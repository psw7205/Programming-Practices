#include <iostream>
using namespace std;

#include <string>

int total_num = 0;
class Student
{
	int num;
	string name;

	void setNum()
	{
		total_num++;
		num = total_num;
	}
public:
	Student()					// default constructor
	{
		name ="noname";
		setNum();
		score = 0;
		cout<<name<<" is created"<<endl;
	}
	Student(string in_name)
	{
		name = in_name;
		setNum();
		score = 0;
		cout<<name<<" is created"<<endl;
	}
	Student(string in_name, float in_score)
	{
		name = in_name;
		score = in_score;
		setNum();
		cout<<name<<" is created"<<endl;
	}
	~Student()
	{
		cout<<name<<" is destructed"<<endl;
	}


	float score;

	void print();
};

void Student::print()
{
	cout<<"Name:"<<name<<endl;
	cout<<"Num:"<<num<<endl;
	cout<<"Score:"<<score<<endl;
}

Student g("global");


class SmartArray
{
	int size;
	int * data;
public:
	SmartArray(int s)
	{
		size = s;
		data = (int *) malloc(sizeof(int)*size);
	}
	~SmartArray()
	{
		free(data);
	}

	int & operator[](int ind)
	{
		return data[ind];
	}

};


void func()
{
	Student l("local");
}
int main()
{
	Student a("Kim",100), b("Lee"), c;
	b.score = 80;

	for(int i=0; i<3; i++)
	{
		Student d("d");
	}
	a.print();
	b.print();
	c.print();
	func();

	SmartArray arr(100);
	arr[10] = 0;
	arr[1] = 10;
	cout<<arr[10]<<endl;

	return 0;
}