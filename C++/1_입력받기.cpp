#include<iostream>
using namespace std;

int main()
{
	int age;
	double score;
	
	
	printf("Input Age : ");
	scanf_s("%d", &age);
	printf("Age : %d\n", age);
	//기존 C방식 자로형에 따라 %d, %f등 연산자를 맞춰야함 
	

	cin >> age >> score;
	cout << "your age is " << age << endl;
	cout << "your score is " << score << endl;
	
	// C와는 다르게 >> 가 알아서 다 맞춰줌

	return 0;
}