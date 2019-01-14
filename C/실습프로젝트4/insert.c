#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "my_struct.h"
#include "my_define.h"
#include "my_func.h"

void Registration(INFO **ar, int *n, int max) // 정보저장
{
	char tmp[3][101];
	int i, j;
	if (*n == max) // 이미 최대 max개가 저장되어있으면
	{
		printf("OVERFLOW\n"); // 오버플로 출력 후
		return; // 조기리턴
	}
	printf("Name:");
	gets(tmp[0]); // 이름입력
	printf("Phone_number:");
	gets(tmp[1]); // 전화번호 입력
	printf("Birth:");
	gets(tmp[2]); // 생일입력

	if (*n == 0) // 처음 저장될 경우
	{
		ar[0] = (INFO*)malloc(sizeof(INFO));

		ar[0]->name = (char*)malloc(sizeof(char)*(strlen(tmp[0]) + 1));
		strcpy(ar[0]->name, tmp[0]);

		ar[0]->phoneNumber = (char*)malloc(sizeof(char)*(strlen(tmp[1]) + 1));
		strcpy(ar[0]->phoneNumber, tmp[1]);

		ar[0]->birthDay = (char*)malloc(sizeof(char)*(strlen(tmp[2]) + 1));
		strcpy(ar[0]->birthDay, tmp[2]); // 값 복사
	}
	else // 2번째 저장될 정보부터는
	{
		for (i = 0; i < *n; i++) // 정보를 확인하며
		{
			if (strcmp(tmp[0], ar[i]->name) < 0) // 더 큰 값이 나올때까지 i이동
				break; // i가 저장될 위치
		}

		for (j = *n; j > i; j--) // 한칸씩 뒤로 이동
			ar[j] = ar[j - 1];

		ar[i] = (INFO*)malloc(sizeof(INFO));

		ar[i]->name = (char*)malloc(sizeof(char)*(strlen(tmp[0]) + 1));
		strcpy(ar[i]->name, tmp[0]);

		ar[i]->phoneNumber = (char*)malloc(sizeof(char)*(strlen(tmp[1]) + 1));
		strcpy(ar[i]->phoneNumber, tmp[1]);

		ar[i]->birthDay = (char*)malloc(sizeof(char)*(strlen(tmp[2]) + 1));
		strcpy(ar[i]->birthDay, tmp[2]); // 값 복사 // i자리에 값 복사
	}

	(*n)++; // 갯수 증가
	printf("<<%d>>\n", *n); // 갯수 출력
	return;
}


void RegFromFile(INFO **ar, int *n, int max)
{
	FILE *fp = fopen("PHONE_BOOK.txt", "r");
	int i, j;
	char tmp[3][101];

	while (fscanf(fp, "%s %s %s", tmp[0], tmp[1], tmp[2]) != EOF)
	{
		if (*n == max) // 이미 최대 max개가 저장되어있으면
		{
			printf("OVERFLOW\n"); // 오버플로 출력 후
			return;
		}

		if (*n == 0) // 처음 저장될 경우
		{
			ar[0] = (INFO*)malloc(sizeof(INFO));

			ar[0]->name = (char*)malloc(sizeof(char)*(strlen(tmp[0]) + 1));
			strcpy(ar[0]->name, tmp[0]);

			ar[0]->phoneNumber = (char*)malloc(sizeof(char)*(strlen(tmp[1]) + 1));
			strcpy(ar[0]->phoneNumber, tmp[1]);

			ar[0]->birthDay = (char*)malloc(sizeof(char)*(strlen(tmp[2]) + 1));
			strcpy(ar[0]->birthDay, tmp[2]); // 값 복사
		}
		else // 2번째 저장될 정보부터는
		{
			for (i = 0; i < *n; i++) // 정보를 확인하며
			{
				if (strcmp(tmp[0], ar[i]->name) < 0) // 더 큰 값이 나올때까지 i이동
					break; // i가 저장될 위치
			}

			for (j = *n; j > i; j--) // 한칸씩 뒤로 이동
				ar[j] = ar[j - 1];

			ar[i] = (INFO*)malloc(sizeof(INFO));

			ar[i]->name = (char*)malloc(sizeof(char)*(strlen(tmp[0]) + 1));
			strcpy(ar[i]->name, tmp[0]);

			ar[i]->phoneNumber = (char*)malloc(sizeof(char)*(strlen(tmp[1]) + 1));
			strcpy(ar[i]->phoneNumber, tmp[1]);

			ar[i]->birthDay = (char*)malloc(sizeof(char)*(strlen(tmp[2]) + 1));
			strcpy(ar[i]->birthDay, tmp[2]); // 값 복사 // i자리에 값 복사
		}
		(*n)++; // 갯수 증가
	}

	fclose(fp);
}

void close(INFO **ar, int *n)
{
	FILE *fp = fopen("PHONE_BOOK.txt", "w");

	for (int i = 0; i < *n; i++)
	{
		fprintf(fp, "%s %s %s\n", ar[i]->name, ar[i]->phoneNumber, ar[i]->birthDay);
	}

	fclose(fp);
}