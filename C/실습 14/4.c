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

	fp2 = fopen(fileName2, "r");
	fp = fopen(fileName, "a");
	if (fp == NULL)
		return -1;


	ch = fgetc(fp2);

	while (!feof(fp2))
	{
		fputc(ch, fp);
		ch = fgetc(fp2);
	}

	fclose(fp);
	fclose(fp2);

	return 0;
}