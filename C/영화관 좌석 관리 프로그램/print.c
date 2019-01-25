#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "structList.h"
#include "functionList.h"

void printCinema(VIEW *view, NODE *head)
{
	NODE *it = head;

	for (int i = 0; i < 8; i++)
	{
		for (int j = 0; j < 8; j++)
		{
			if (j == 2 || j == 6)
				printf("  ");

			if (view->cinema[i][j] == 0)
				printf("-- ");
			else
				printf("¡á ");
		}
		printf(" %c %d", it->name, it->price);
		it = it->next;
		printf("\n");
	}
}

void sortByName(INFO *info, int *n)
{
	INFO tmp;
	for (int i = 0; i < *n - 1; i++)
	{
		for (int j = 0; j < *n - 1 - i; j++)
		{
			if (strcmp(info[j].name, info[j + 1].name) > 0)
			{
				tmp = info[j];
				info[j] = info[j + 1];
				info[j + 1] = tmp;
			}
		}
	}
}

void printInfo(INFO *info, int *n)
{
	for (int i = 0; i < *n; i++)
	{
		printf("%s, ÁÂ¼® (%c, %d), °¡°Ý : %d\n",
			info[i].name, info[i].row + 'A', info[i].col, info[i].price);
	}
}