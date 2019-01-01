#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "my_struct.h"
#include "my_define.h"
#include "my_func.h"

void ShowAll(INFO **ar, int *n)
{
	int i;

	for (i = 0; i < *n; i++) // 배열을 순회하며 데이터 출력
	{
		printf("%s %s %s\n", ar[i]->name, ar[i]->phoneNumber, ar[i]->birthDay);
	}
}

void FindByBirth(INFO **ar, int *n)
{
	int i, tmp, mon = 0;

	printf("Birth:");
	scanf("%d", &tmp); // 생일을 입력받으면
	for (i = 0; i < *n; i++)
	{
		mon = ar[i]->birthDay[4] - '0'; // 10의 자리를 int형 변수에 저장 후
		mon *= 10; // *10을 통해 10의 자리로 이동
		mon += ar[i]->birthDay[5] - '0'; // 1의 자리 저장, 이 연산을 통해 생일을 정수로 저장

		if (mon == tmp) // 찾는 생일이 나오면
			printf("%s %s %s\n", ar[i]->name, ar[i]->phoneNumber, ar[i]->birthDay); // 해당 데이터 출력
	}
}