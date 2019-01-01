#include <stdio.h>
#pragma warning(disable:4996)

int main()
{
	char fileName[21];
	char fileName2[21];
	char ch;
	FILE* fp = NULL;
	FILE* fp2 = NULL;

	scanf("%s %s", fileName, fileName2);

	fp2 = fopen(fileName2, "w");
	fp = fopen(fileName, "r");
	if (fp == NULL)
		return -1;


	ch = fgetc(fp);

	while (!feof(fp))
	{
		fputc(ch, fp2);
		ch = fgetc(fp);
	}

	fclose(fp);
	fclose(fp2);

	return 0;
}