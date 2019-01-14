#include <iostream>
#include <cstring>
using namespace std;

class Book
{
	char *title;
	int price;
public:
	Book(const char* title, int price);
	Book(Book &a);
	~Book();
	void set(char* title, int price);
	void show() { cout << title << " " << price << "원" << endl; }
};

Book::Book(const char * title, int price)
{
	int size = strlen(title); // 글자 수를 구하고
	this->title = new char[size+1]; // 그 크기+1 만큼 동적할당합니다.
	strcpy(this->title, title); // 문자열을 복사합니다.
	this->price = price; // 가격을 복사합니다. 
}

void Book::set(char*title, int price)
{
	strcpy(this->title, title);
	this->price = price;
}

Book::~Book()
{
	delete[] title;
}

Book::Book(Book &a)
{
	int size = strlen(a.title); 
	this->title = new char[size+1]; 
	strcpy(this->title, a.title);
	this->price = price;
} // 깊은 복사를 위해 새롭게 동적할당 후 데이터를 복사합니다.

int main()
{
	Book cpp("명품 C++", 10000);
	Book java = cpp;
	java.set("명품자바",12000);
	cpp.show();
	java.show();

	return 0;
}