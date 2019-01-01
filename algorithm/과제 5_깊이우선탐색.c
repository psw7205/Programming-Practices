#include <stdio.h>
#include <memory.h>
#include <stdlib.h>
#define MAX_VERTEX 10
#define FALSE 0
#define TRUE 1

typedef struct graphNode {    //그래프에 대한 인접 리스트의 노드 구조 정의
	int vertex;
	struct graphNode* link;
} graphNode;

typedef struct graphType {
	int n;                   //정점의 갯수
	graphNode* adjList_H[MAX_VERTEX];   //정점에 대한 인접 리스트의 헤드 노드 배열
	int visited[MAX_VERTEX];              //정점에 대한 방문 표시를 위한 배열
}graphType;

//////// << 스택 연산
typedef struct stackNode {
	int data;
	struct stackNode *link;
}stackNode;

stackNode* top;

void push(int item)
{
	stackNode* temp = (stackNode *)malloc(sizeof(stackNode));
	temp->data = item;
	temp->link = top;
	top = temp;
}

int pop()
{
	int item;
	stackNode* temp = top;

	if (top == NULL) {
		printf("\n\n Stack is empty !\n");
		return -1;
	}
	else {
		item = temp->data;
		top = temp->link;
		free(temp);
		return item;
	}
}
//////// 스택 연산 >>

void createGraph(graphType* g)       //깊이 우선 탐색을 위한 초기 공백 그래프 생성 연산
{
	int v;
	g->n = 0;                      //그래프의 정점 개수를 0으로 초기화
	for (v = 0; v<MAX_VERTEX; v++) {
		g->visited[v] = FALSE;        //그래프의 정점에 대한 배열 visited를 FALSE로 초기화
		g->adjList_H[v] = NULL;       //인접 리스트에 대한 헤드 노드 배열을 NULL로 초기화
	}
}

void insertVertex(graphType* g, int v)   //그래프 g에 정점 v를 삽입하는 연산
{
	if (((g->n) + 1)>MAX_VERTEX) {
		printf("\n 그래프 정점의 개수를 초과하였습니다!");
		return;
	}
	g->n++;
}

void insertEdge(graphType* g, int u, int v)  //그래프 g에 간선 (u, v)를 삽입하는 연산
{
	graphNode* node;
	if (u >= g->n || v >= g->n) {
		printf("\n 그래프에 없는 정점입니다!");
		return;
	}
	node = (graphNode *)malloc(sizeof(graphNode));
	node->vertex = v;
	node->link = g->adjList_H[u];
	g->adjList_H[u] = node;
}

void print_adjList(graphType* g)    //그래프 g에 대한 인접 리스트를 출력하는 연산
{
	int i;
	graphNode* p;
	for (i = 0; i<g->n; i++) {
		printf("\n\t정점 %d의 인접 리스트", i);
		p = g->adjList_H[i];
		while (p) {
			printf(" -> %d", p->vertex );
			p = p->link;
		}
	}
}

void DFS_adjList(graphType* g, int v)    //그래프 g에서 정점 v에 대한 깊이 우선 탐색 연산
{
	graphNode* w; // v는 현재 정점, w는 노드를 가르키는 포인터변수
	top = NULL;   // 스택 top 설정
	g->visited[v] = TRUE;
	
	//printf(" %d", v); // 출발 정점은 바로 처리, w는 아직 노드를 가르키고 있지 않습니다.

	while (v != -1) //스택이 공백이 아닌 동안 깊이 우선 탐색 반복, 스텍이 공백이면 -1을 리턴합니다.
	{      
		w = g->adjList_H[v]; // 정점 v를 헤드노드 라인으로 이동시킴
		
		while (w) // 인접정점이 있는 동안 수행
		{
			if (g->visited[w->vertex] == 0)   //1) 현재 정점 w를 방문하지 않은 경우
			{ 
				push(v); // 현재 노드를 push
				g->visited[w->vertex] = TRUE; // visited배열에 방문했다고 표시
				printf(" %d", w->vertex); // 정점 출력
				v = w->vertex; // 방문한 신규 노드로 이동
				w = g->adjList_H[v]; // 신규노드의 헤드라인으로 이동
			}
			else //2) 현재 정점 w가 이미 방문한 정점인 경우
			{
				printf(" %d", w->vertex); // w의 이동을 확인하기 위해 w를 다음 정점으로 이동 전에 출력하는 것을 추가했습니다.
				w = w->link; // 다음 정점으로 이동
			}
		}
		v = pop(); //현재 정점에서 더 이상 순회를 진행할 인접 정점이 없는 경우에 스택 pop
	}
}

void main()
{
	int i;
	graphType *G4 = (graphType *)malloc(sizeof(graphType));;
	createGraph(G4);

	for (i = 0; i<5; i++)        //그래프 G5 구성
		insertVertex(G4, i);

	insertEdge(G4, 0, 2);
	insertEdge(G4, 0, 1);
	insertEdge(G4, 1, 3);
	insertEdge(G4, 1, 2);
	insertEdge(G4, 1, 0);
	insertEdge(G4, 2, 4);
	insertEdge(G4, 2, 3);
	insertEdge(G4, 2, 1);
	insertEdge(G4, 2, 0);
	insertEdge(G4, 3, 2);
	insertEdge(G4, 3, 1);
	insertEdge(G4, 4, 2);
	printf("\n G4의 인접 리스트 ");
	print_adjList(G4);

	printf("\n\n///////////////\n\n깊이 우선 탐색시 w의 위치 추적 >> ");
	DFS_adjList(G4, 0);     //0번 정점인 정점 A에서 깊이 우선 탐색 시작
	
	printf("\n");
	
}
