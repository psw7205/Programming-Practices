#include <stdio.h>
#pragma warning(disable:4996)

typedef struct student {
	char name[11];
	int score;
}STU;

int main()
{
	STU ar[3];
	FILE* fp = fopen("student.bat", "rb");

	fread(ar, sizeof(STU), 3, fp);

	for (int i = 0; i < 3; i++)
	{
		printf("%s %d\n", ar[i].name, ar[i].score);
	}

	fclose(fp);

	return 0;
}