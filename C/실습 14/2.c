#include <stdio.h>
#pragma warning(disable:4996)

int main()
{
	char ch;
	FILE* fp2 = fopen("test2.txt", "w");
	FILE* fp = fopen("test1.txt", "r");
	if (fp == NULL)
		return -1;

	fscanf(fp, "%c", &ch);

	while (!feof(fp))
	{
		if (ch >= 'a' && ch <= 'z')
			ch += 'A' - 'a';
		else if (ch >= 'A' && ch <= 'Z')
			ch += 'a' - 'A';

		fprintf(fp2, "%c", ch);
		fscanf(fp, "%c", &ch);

	}

	return 0;
}
