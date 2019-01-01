#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "my_struct.h"
#include "my_define.h"
#include "my_func.h"

void MyDelete(INFO **ar, int *n)
{
	char tmp[101];
	int i, j;

	if (*n == 0) // 데이터가 없으면 종료
	{
		printf("NO MEMBER\n");
		return;
	}

	printf("Name:");
	gets(tmp); // 지울 이름 저장

	for (i = 0; i < *n; i++)
	{
		if (!strcmp(tmp, ar[i]->name)) // 같은 이름을 찾으면
			break; // 탈출
	}

	if (i == *n) // i가 n까지 증가했으면 같은 이름을 못찾은 것
		return; // 리턴

	free(ar[i]->birthDay);
	free(ar[i]->name);
	free(ar[i]->phoneNumber);
	free(ar[i]);

	for (j = i; j < *n; j++) // 찾은 자리를 한칸식 앞으로 이동시켜 삭제
		ar[j] = ar[j + 1];

	(*n)--; // 갯수 감소

	return;
}