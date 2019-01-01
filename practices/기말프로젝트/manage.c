#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "structList.h"
#include "functionList.h"

void initView(VIEW *in)
{
	for (int i = 0; i < 8; i++)
		for (int j = 0; j < 8; j++)
			in->cinema[i][j] = 0;
}

NODE* getNode()
{
	NODE* newLine = (NODE*)malloc(sizeof(NODE));
	newLine->name = 'A';
	newLine->price = 9000;
	newLine->next = NULL;
	return newLine;
}

void insertNODE(NODE** head, int i)
{
	NODE *newLine = getNode();
	NODE *it = *head;

	if (i == 0)
	{
		*head = newLine;
		return;
	}

	newLine->name = i + 'A';

	switch (i)
	{
	case 0:	case 1: case 7:
		newLine->price = 9000;
		break;
	case 2: case 3:
		newLine->price = 10000;
		break;
	case 4: case 5: case 6:
		newLine->price = 11000;
		break;
	default:
		break;
	}

	while (it->next != NULL)
	{
		it = it->next;
	}

	it->next = newLine;
	return;
}

NODE* initCinema()
{
	NODE *tmp = NULL;
	for (int i = 0; i < 8; i++)
	{
		insertNODE(&tmp, i);
	}

	return tmp;
}

void reservation(VIEW *view, INFO *info, NODE *head, int *num)
{
	char name[21];
	int col;
	char row;
	NODE *it = head;

	printCinema(view, head);

	if (*num == 64)
	{
		printf("관람객을 더이상 받을 수 없습니다\n");
		return;
	}

	while (1)
	{
		printf("이름 : ");
		scanf("%s", name);
		getchar();
		printf("좌석번호 : ");
		scanf("%c%d", &row, &col);

		if (row >= 'a' && row <= 'z')
			row -= 'a';
		else if (row >= 'A' && row <= 'Z')
			row -= 'A';

		if (view->cinema[(int)row][col - 1] == 0 && row < 8 && col <= 8 && row >= 0 && col > 0)
		{
			view->cinema[(int)row][col - 1] = 1;
			strcpy(info[*num].name, name);
			info[*num].row = row;
			info[*num].col = col;

			while (it != NULL)
			{
				if (it->name - 'A' == row)
				{
					info[*num].price = it->price;
					break;
				}
				it = it->next;
			}
			printf("가격은 %d입니다\n", info[*num].price);
			(*num)++;
			return;
		}
		else
		{
			printf("예약이 불가능한 좌석입니다. 다시 입력하세요\n");
		}
	}
}

void deleteList(VIEW *view, INFO *info, int *n)
{
	char tmp[21];
	int i, j;

	if (*n == 0)
	{
		printf("예약된 사람이 없습니다.\n");
		return;
	}

	scanf("%s", tmp);

	for (i = 0; i < *n; i++)
	{
		if (!strcmp(tmp, info[i].name))
			break;
	}

	if (i == *n)
	{
		printf("잘못된 이름입니다.\n");
		return;
	}

	view->cinema[info[i].row][info[i].col-1] = 0;

	for (j = i; j < *n; j++)
		info[j] = info[j + 1];

	(*n)--;
	printf("삭제되었습니다.\n");
}