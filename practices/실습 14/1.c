#include <stdio.h>
#pragma warning(disable:4996)

int main()
{
	int cnt = 0, sum = 0, tmp;
	double avg = 0.0;
	FILE* fp = fopen("data.txt", "w");

	while (1)
	{
		scanf("%d", &tmp);
		if (tmp == -99)
			break;
		fprintf(fp, "%d\n", tmp);
	}

	fclose(fp);

	fp = fopen("data.txt", "r");

	fscanf(fp, "%d", &tmp);

	while (!feof(fp))
	{
		sum += tmp;
		cnt++;
		fscanf(fp, "%d", &tmp);
	}

	avg = (double)sum / cnt;

	printf("%d\n", cnt);
	printf("%d\n", sum);
	printf("%.2f\n", avg);

	fclose(fp);
	return 0;
}