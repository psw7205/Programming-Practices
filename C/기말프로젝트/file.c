#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "structList.h"
#include "functionList.h"

void fileStore(VIEW *view, NODE *head, INFO *info, int *n)
{
	FILE *fp;
	NODE *it = head;
	fp = fopen("Theater.txt", "w");

	int i, j;
	for (i = 0; i < 8; i++)
	{
		for (j = 0; j < 8; j++)
		{
			if (j == 2 || j == 6)
				fprintf(fp, "  ");

			if (view->cinema[i][j] == 0)
				fprintf(fp, "- ");
			else
				fprintf(fp, "■ ");
		}
		fprintf(fp, " %c %d", it->name, it->price);
		it = it->next;
		fprintf(fp, "\n");
	}

	for (int i = 0; i < *n; i++)
	{
		fprintf(fp, "%s, (%c, %d), 가격 : %d\n",
			info[i].name, info[i].row + 'A', info[i].col, info[i].price);
	}

	fclose(fp);

	fp = fopen("list.bat", "wb");
	fwrite(info, sizeof(INFO), 64, fp);
	fwrite(n, sizeof(int), 1, fp);

	fclose(fp);
}

void fileLoad(INFO *info, VIEW *view, int *n)
{
	FILE *fp;
	fp = fopen("list.bat", "rb");

	if (fp == NULL)
	{
		printf("파일이 없습니다.");
		return;
	}

	fread(info, sizeof(INFO), 64, fp);
	fread(n, sizeof(int), 1, fp);

	for (int i = 0; i < *n; i++)
	{
		view->cinema[info[i].row][info[i].col - 1] = 1;
	}

	fclose(fp);
}
