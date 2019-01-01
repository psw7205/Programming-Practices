#include<stdio.h>
#pragma warning(disable: 4996)

int main()
{
	int arry[100];
	int  n, m, sp, fp;


	scanf("%d", &n);

	for (int i = 0; i < n; i++)
	{
		scanf("%d", &arry[i]);
	}

	scanf("%d", &m);

	for (int i = 0; i < m; i++)
	{
		scanf("%d", &sp);
		scanf("%d", &fp);
		int n = fp - sp + 1;
		for (int j = 0; j < n / 2; j++)
		{
			int temp;
			temp = arry[sp];
			arry[sp] = arry[fp];
			arry[fp] = temp;
			sp++;
			fp--;
		}
	}
	for (int i = 0; i < n; i++)
	{
		printf(" %d", arry[i]);
	}

	return 0;
}