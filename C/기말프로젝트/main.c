#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "structList.h"
#include "functionList.h"

int main()
{
	INFO info[64];
	NODE *cinema = initCinema();
	VIEW view;
	int menu, menu2, num = 0;
	char ch;
	initView(&view);

	printf("이전 파일을 불러오시겠습니까? (Y/N) ");
	scanf("%c", &ch);
	if (ch == 'Y')
		fileLoad(info, &view, &num);

	while (1)
	{
		printf("\n세종영화관 예약 시스템입니다.\n");
		printf("[1.예약] [2.조회] [3.예약취소] [4.종료]\n");
		printf("번호를 입력하세요 : ");
		scanf("%d", &menu);
		getchar();

		if (menu == 4)
		{
			fileStore(&view, cinema, info, &num);
			break;
		}

		switch (menu)
		{
		case 1:
			reservation(&view, info, cinema, &num);
			break;
		case 2:
			printf("조회-> [1.전체 조회] [2.이름 순 조회]\n");
			printf("번호를 입력하세요 : ");

			scanf("%d", &menu2);
			getchar();

			switch (menu2)
			{
			case 1:
				printCinema(&view, cinema);
				break;
			case 2:
				sortByName(info, &num);
				printInfo(info, &num);
				break;
			default:
				break;
			}
			break;
		case 3:
			printf("삭제할 이름을 입력하세요 : ");
			deleteList(&view, info, &num);
			break;
		default:
			printf("잘못된 메뉴입니다. 다시 입력하세요\n");
			while (getchar() != '\n');
			break;
		}
	}

	for (int i = 0; i < 8; i++)
	{
		NODE *tmp = cinema;
		cinema = cinema->next;
		free(tmp);
	}
	
	return 0;
}