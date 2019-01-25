#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "my_struct.h"
#include "my_define.h"
#include "my_func.h"

int main()
{
	INFO **ar; // 총 max_num개의 구조체 배열
	int size = 0; // 현재 갯수
	int selectMenu;
	int max_num; // 최대 갯수 

	printf("Max_num:"); // 고정
	scanf("%d", &max_num);
	getchar();

	ar = (INFO**)malloc(sizeof(INFO*)*max_num);

	if (ar == NULL)
		return -1;

	while (1)
	{
		printf("*****Menu*****\n");
		printf("<1.Registration><2.ShowAll><3.Delete><4.FindByBirth><5.RegFromFile><6.Exit>\n");
		printf("Enter_the_menu_number:");

		scanf("%d", &selectMenu);
		getchar();

		if (selectMenu == 6)
		{
			close(ar, &size);
			break;
		}

		switch (selectMenu) // 메뉴에 맞는 함수 실행
		{
		case 1:
			Registration(ar, &size, max_num);
			break;
		case 2:
			ShowAll(ar, &size);
			break;
		case 3:
			MyDelete(ar, &size);
			break;
		case 4:
			FindByBirth(ar, &size);
			break;
		case 5:
			RegFromFile(ar, &size, max_num);
			break;
		default:
			break;
		}
	}


	for (int i = 0; i < size; i++)
	{
		free(ar[i]->birthDay);
		free(ar[i]->name);
		free(ar[i]->phoneNumber);
		free(ar[i]);
	}

	free(ar);

	return 0;
}