// 2019년 1학기 네트워크프로그래밍 퀴즈 2번
// 성명: 박상우 학번: 16013093
// 플랫폼: Visual Studio 2017

#define _WINSOCK_DEPRECATED_NO_WARNINGS // 최신 VC++ 컴파일 시 경고 방지
#pragma comment(lib, "ws2_32")
#pragma warning(disable:4996)
#include <winsock2.h>
#include <stdlib.h>
#include <stdio.h>

#define SERVERIP   "127.0.0.1"
#define SERVERPORT 9000
#define BUFSIZE    512

typedef struct Nums {
	int first;
	int second;
}Nums;

// 소켓 함수 오류 출력 후 종료
void err_quit(char *msg)
{
	LPVOID lpMsgBuf;
	FormatMessage(
		FORMAT_MESSAGE_ALLOCATE_BUFFER | FORMAT_MESSAGE_FROM_SYSTEM,
		NULL, WSAGetLastError(),
		MAKELANGID(LANG_NEUTRAL, SUBLANG_DEFAULT),
		(LPTSTR)&lpMsgBuf, 0, NULL);
	MessageBox(NULL, (LPCTSTR)lpMsgBuf, msg, MB_ICONERROR);
	LocalFree(lpMsgBuf);
	exit(1);
}

// 소켓 함수 오류 출력
void err_display(char *msg)
{
	LPVOID lpMsgBuf;
	FormatMessage(
		FORMAT_MESSAGE_ALLOCATE_BUFFER | FORMAT_MESSAGE_FROM_SYSTEM,
		NULL, WSAGetLastError(),
		MAKELANGID(LANG_NEUTRAL, SUBLANG_DEFAULT),
		(LPTSTR)&lpMsgBuf, 0, NULL);
	printf("[%s] %s", msg, (char *)lpMsgBuf);
	LocalFree(lpMsgBuf);
}

// 사용자 정의 데이터 수신 함수
int recvn(SOCKET s, char *buf, int len, int flags)
{
	int received;
	char *ptr = buf;
	int left = len;

	while (left > 0) {
		received = recv(s, ptr, left, flags);
		if (received == SOCKET_ERROR)
			return SOCKET_ERROR;
		else if (received == 0)
			break;
		left -= received;
		ptr += received;
	}

	return (len - left);
}

int main(int argc, char *argv[])
{
	int retval;

	// 윈속 초기화
	WSADATA wsa;
	if (WSAStartup(MAKEWORD(2, 2), &wsa) != 0)
		return 1;

	// socket()
	SOCKET sock = socket(AF_INET, SOCK_STREAM, 0);
	if (sock == INVALID_SOCKET) err_quit(const_cast<char*>("socket()"));

	// connect()
	SOCKADDR_IN serveraddr;
	ZeroMemory(&serveraddr, sizeof(serveraddr));
	serveraddr.sin_family = AF_INET;
	serveraddr.sin_addr.s_addr = inet_addr(SERVERIP);
	serveraddr.sin_port = htons(SERVERPORT);
	retval = connect(sock, (SOCKADDR *)&serveraddr, sizeof(serveraddr));
	if (retval == SOCKET_ERROR) err_quit(const_cast<char*>("connect()"));

	// 데이터 통신에 사용할 변수
	Nums data;
	int result;

	// 서버와 데이터 통신
	while (1) {
		// 데이터 입력
		printf("\n두 정수 입력(문자 입력시 프로그램 종료) >> ");

		char tmp;
		if (scanf("%d %d", &data.first, &data.second) == NULL)
		{
			printf("잘못된 값 입력 프로그램을 종료합니다\n");
			break;
		}

		// 숫자 2개 이상 입력시 2개를 제외하곤 입력 버퍼 비우기
		while ((tmp = getchar()) != EOF && tmp != '\n');

		// 데이터 보내기
		retval = send(sock, (char*)&data, sizeof(data), 0);
		if (retval == SOCKET_ERROR) {
			err_display(const_cast<char*>("send()"));
			break;
		}
		printf("[TCP 클라이언트] %d바이트를 보냈습니다.\n", sizeof(data));

		// 데이터 받기
		retval = recvn(sock, (char*)&result, sizeof(result), 0);
		if (retval == SOCKET_ERROR) {
			err_display(const_cast<char*>("recv()"));
			break;
		}
		else if (retval == 0)
			break;

		// 받은 데이터 출력
		// 서버에서 두 수의 합을 계산하여 리턴
		printf("[TCP 클라이언트] %d바이트를 받았습니다.\n", sizeof(result));
		printf("[받은 데이터] %d\n", result);
	}

	// closesocket()
	closesocket(sock);

	// 윈속 종료
	WSACleanup();
	return 0;
}
