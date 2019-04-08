// 2019년 1학기 네트워크프로그래밍 숙제 1번 서버
// 성명: 박상우 학번: 16013093
// 플랫폼: VS2017
// 작동하는 도메인 네임
// www.naver.com
// www.daum.net
// www.amazon.com
// stackoverflow.com

// Aliases의 길이가 50보다 긴 도메인
// www.apple.com
// www.ibm.com
// www.microsoft.com

#define _WINSOCK_DEPRECATED_NO_WARNINGS // 최신 VC++ 컴파일 시 경고 방지
#pragma comment(lib, "ws2_32")
#include <winsock2.h>
#include <stdlib.h>
#include <stdio.h>

#define SERVERPORT 9000
#define BUFSIZE    512

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

// 데이터를 보낼 때 사용하는 함수입니다.
void sendFixedVariableData(SOCKET client_sock, char *buf, int len)
{
	// 데이터 보내기(고정 길이)
	int retval = send(client_sock, (char *)&len, sizeof(int), 0);
	if (retval == SOCKET_ERROR) {
		err_display(const_cast<char*>("send()"));
		return;
	}

	// 데이터 보내기(가변 길이)
	retval = send(client_sock, buf, len, 0);
	if (retval == SOCKET_ERROR) {
		err_display(const_cast<char*>("send()"));
		return;
	}
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

	// bind()
	SOCKADDR_IN serveraddr;
	ZeroMemory(&serveraddr, sizeof(serveraddr));
	serveraddr.sin_family = AF_INET;
	serveraddr.sin_addr.s_addr = htonl(INADDR_ANY);
	serveraddr.sin_port = htons(SERVERPORT);
	retval = bind(sock, (SOCKADDR *)&serveraddr, sizeof(serveraddr));
	if (retval == SOCKET_ERROR) err_quit(const_cast<char*>("bind()"));

	// listen()
	retval = listen(sock, SOMAXCONN);
	if (retval == SOCKET_ERROR) err_quit(const_cast<char*>("listen()"));

	// 데이터 통신에 사용할 변수
	SOCKET client_sock;
	SOCKADDR_IN clientaddr;
	int addrlen;
	char buf[BUFSIZE + 1];
	int len;

	bool flag = 0;

	HOSTENT *hostData;

	while (1) {
		// accept()
		addrlen = sizeof(clientaddr);
		client_sock = accept(sock, (SOCKADDR *)&clientaddr, &addrlen);
		if (client_sock == INVALID_SOCKET) {
			err_display(const_cast<char*>("accept()"));
			break;
		}

		// 접속한 클라이언트 정보 출력
		printf("\n[TCP 서버] 클라이언트 접속: IP 주소=%s, 포트 번호=%d\n",
			inet_ntoa(clientaddr.sin_addr), ntohs(clientaddr.sin_port));

		// 클라이언트와 데이터 통신
		while (1) {
			// 데이터 받기(고정 길이)
			retval = recvn(client_sock, (char *)&len, sizeof(int), 0);
			if (retval == SOCKET_ERROR) {
				err_display(const_cast<char*>("recv()"));
				break;
			}
			else if (retval == 0)
				break;

			// 데이터 받기(가변 길이)
			retval = recvn(client_sock, buf, len, 0);
			if (retval == SOCKET_ERROR) {
				err_display(const_cast<char*>("recv()"));
				break;
			}
			else if (retval == 0)
				break;

			// 받은 데이터 출력
			buf[retval] = '\0';
			printf("\n[TCP/%s:%d] %s\n", inet_ntoa(clientaddr.sin_addr),
				ntohs(clientaddr.sin_port), buf);

			// quit가 입력되면 서버도 종료
			if (!strcmp(buf, "quit"))
			{
				flag = true;
				break;
			}

			// 호스트 이름 얻기
			hostData = gethostbyname(buf);

			// 호스트 이름이 없거나 클라이언트에서 바로 return시 오류처리
			if (hostData == NULL || !strcmp(buf, "")) 
			{
				char *errMsg = const_cast<char*>("잘못된 호스트 네임입니다.");
				printf("%s\n", errMsg);
				sendFixedVariableData(client_sock, errMsg, (int)strlen(errMsg));
			}
			else
			{	
			// 데이터 출력 후 클라이언트로 데이터 전송
				printf("### Domain Name : \t");
				printf("%s\n", buf);
				sendFixedVariableData(client_sock, buf, (int)strlen(buf));

				printf("### Official Name : \t");
				char *ptr1 = hostData->h_name;
				printf("%s\n", ptr1);
				sendFixedVariableData(client_sock, ptr1, (int)strlen(ptr1));

				printf("### Aliases ###\n");
				char **ptr2 = hostData->h_aliases;
				while (*ptr2) {
					printf("%s\n", *ptr2);
					sendFixedVariableData(client_sock, *ptr2, (int)strlen(*ptr2));
					++ptr2;
				}

				printf("### IP addresses ###\n");
				IN_ADDR addr;
				char **ptr3 = hostData->h_addr_list;
				while (*ptr3) {
					memcpy(&addr, *ptr3, hostData->h_length);
					printf("%s\n", inet_ntoa(addr));
					sendFixedVariableData(client_sock, inet_ntoa(addr), (int)strlen(inet_ntoa(addr)));
					++ptr3;
				}

				char *msg = const_cast<char*>("데이터 전송 완료");
				sendFixedVariableData(client_sock, msg, (int)strlen(msg));
			}
			
		}

		// closesocket()
		closesocket(client_sock);
		printf("[TCP 서버] 클라이언트 종료: IP 주소=%s, 포트 번호=%d\n",
			inet_ntoa(clientaddr.sin_addr), ntohs(clientaddr.sin_port));

		if (flag == true)
		{
			printf("quit 입력 프로그램을 종료합니다\n");
			break;
		}
	}

	// closesocket()
	closesocket(sock);

	// 윈속 종료
	WSACleanup();
	return 0;
}
