#include <stdio.h>
#pragma warning(disable:4996)

typedef struct student {
	char name[11];
	int score;
}STU;

int main()
{
	STU ar[3];
	FILE* fp = fopen("student.bat", "wb");
	
	for (int i = 0; i < 3; i++)
	{
		scanf("%s %d", ar[i].name, &ar[i].score);
	}

	fwrite(ar, sizeof(STU), 3, fp);
	fclose(fp);

	return 0;
}