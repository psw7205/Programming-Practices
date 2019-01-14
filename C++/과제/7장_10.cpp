#include<iostream>
using namespace std;

class Stack {
	int m_Stack[100];
	int m_n;
	int m_top;
public:
	Stack();
	Stack &operator<< (int a);
	Stack operator>> (int &a);
	bool operator! ();
};

Stack::Stack()
{
	m_top = -1;
}

Stack &Stack::operator<< (int a)
{
	m_top++;
	m_Stack[m_top] = a;
	return *this;
}
Stack Stack::operator>> (int &a)
{
	a = m_Stack[m_top];
	m_top--;
	return *this;
}

bool Stack::operator! ()
{
	if (m_top == -1)
		return true;
	else
		return false;
}

int main()
{
	Stack stack;
	stack << 3 << 5 << 10;

	while (true)
	{
		if (!stack) break;
		int x;
		stack >> x;
		cout << x << " ";
	}

	cout << endl;

	return 0;
}
