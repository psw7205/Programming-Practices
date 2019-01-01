/*
디지털콘텐츠학과 16013093 박상우입니다.
포인터 주소를 이용하여 문자열의 맨처음과 맨뒤 문자가 같으면 count가 1씩 증가하고
최종적으로 문자열 길이와 count가 같으면 palindrome임을 확인하는 방법입니다.
*/

#include<stdio.h>
#include<string.h>
#pragma warning(disable: 4996) // vs2017버전 scanf의 c4996 오류를 무시합니다.


int palindrome(char a[])
{

	int len = 0, count = 0;

	len = strlen(a);

	for (int i = len - 1, j = 0; i >= 0, j < len; i--, j++)
	{
		if (*(a + j) == *(a + i))
			count++;
	}

	if (len == count)
		return 1;
	else
		return 0;
}

int main()
{
	char a[100];
	int b = 0;

	scanf("%s", a);

	printf("입력한 단어 %s는 ", a);

	if (palindrome(a) == 1)
		printf("palindrome 입니다 \n");
	else
		printf("palindrome이 아닙니다 \n");

	return 0;

}