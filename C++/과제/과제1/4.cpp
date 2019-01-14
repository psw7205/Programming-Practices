#include<iostream>
using namespace std;


int main()
{
	float AR[5]; // 실수를 저장할 double형 배열
	float max = 0; // 최대값을 저장할 변수

	cout << "5개의 실수를 입력하라>>" ;

	for (int i = 0; i < 5; i++)
	{
		cin >> AR[i];
	} // AR[0]~AR[4]까지 5개의 실수 입력

	max = AR[0];

	for (int i = 1; i < 5; i++)
	{
		if (max < AR[i])
			max = AR[i];
	} // max가 AR[i]보다 작을 때 AR[i]를 max에 저장

	cout << "제일 큰 수 = " << max << endl;

	return 0;
}
