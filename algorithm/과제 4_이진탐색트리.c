#include<stdio.h> 
#include<stdlib.h> 
#pragma warning(disable:4996)

typedef struct treeNode 
{
	int data;				
	struct treeNode* left;	
	struct treeNode* right;	
} treeNode;

// 이진 탐색 트리에서 키값이 x인 노드의 위치를 탐색하는 연산입니다.
// 기준노드 값 입력받고 root노드에서 기준노드까지 이동하기 위해 사용했습니다.
treeNode* searchtreeNode(treeNode* root, char x) 
{
	treeNode* p = root; 

	while (p != NULL) {

		if (x < p->data) 
			p = p->left; // 원하는 노드의 값이 지금 노드의 값보다 작으면 왼쪽자식노드로 이동합니다.
		else if (x == p->data)
			return p; // 원하는 기준노드까지 이동했으면 기준노드를 리턴합니다.
		else 
			p = p->right; // 아니면 오른쪽 자식노드로 이동합니다.
	}

	printf("찾는 노드가 없습니다!\n");
	return root; // 노드를 못찾았으면 그냥 루트노드를 다시 리턴합니다.
}

// 포인터 p가 가리키는 노드와 비교하여 노드 x를 삽입하는 연산입니다.
treeNode* insertNode(treeNode *p, int x) 
{
	treeNode *newNode;

	if (p == NULL) // p가 가리키는 노드에서 삽입할 위치까지 도달했으면 
	{
		newNode = (treeNode*)malloc(sizeof(treeNode)); // 새로운 노드를 만들고
		newNode->data = x;
		newNode->left = NULL;
		newNode->right = NULL;
		return newNode; // 삽입한 새 노드를 리턴합니다.
	}
	else if (x < p->data)
		p->left = insertNode(p->left, x); // 삽입할 값이 현재노드 데이터보다 작으면 왼쪽자식으로
	else if (x > p->data)
		p->right = insertNode(p->right, x); // 크면 오른쪽 자식으로 재귀호출하며 내려갑니다.
	else
		printf("이미 같은 키가 있습니다!\n");

	return p; // 새노드가 리턴되지 않았다면 중복된 값이 있는 것이고 
	//이진탐색트리에서 같은 값은 중복될 수 없으니 그냥 리턴합니다.
}

treeNode* maxNode(treeNode *p) // 좌측서브트리 중 가장 큰 노드를 찾는 함수입니다.
{
	treeNode* tmp = p; // 앞에서 탐색할 tmp 포인터입니다.
	treeNode* q = NULL; // 실제로 가장 큰 노드를 리턴할 포인터입니다.

	if (tmp->left == NULL) // 기준노드 left가 NULL이면 좌측서브트리가 존재하지 않는 것이고
	{
		printf("기준노드 좌측서브트리가 존재하지 않습니다.\n");
		return tmp; // 기준노드를 리턴합니다.
	}

	tmp = tmp->left; // 위에서 리턴되지 않았으면 좌측서브트리로 이동 후

	while (tmp != NULL) // tmp가 NULL이 아닐 때까지
	{
		q = tmp; // q는 tmp를 저장하고
		tmp = tmp->right; // tmp를 오른쪽 자식으로 이동시킵니다.
	}

	// tmp는 NULL이 되었고 더이상 오른쪽 자식이 없으면 
	return q; //그 노드가 최대 노드이므로 q를 리턴합니다.
}

treeNode* minNode(treeNode *p) // 우측서브트리 중 가장 작은 노드를 찾는 함수입니다.
{// maxNode함수와 방법이 같으며 최초 우측서브트리로 이동 후 마지막 왼쪽 자식까지 이동해 최소 노드를 찾았습니다.
	treeNode* tmp = p;
	treeNode* q = NULL;

	if (tmp->right == NULL)
	{
		printf("기준노드 우측서브트리가 존재하지 않습니다.\n");
		return tmp;
	}

	tmp = tmp->right;

	while (tmp != NULL)
	{
		q = tmp;
		tmp = tmp->left;
	}

	return q;
}

int main()
{
	treeNode* root = NULL; // 루트노드입니다. 
	int  leftMax, rightMin, n; // 좌측서브트리 최대, 우측서브트리 최소, 기준노드의 값을 저장할 변수들입니다. 

	root = insertNode(root, 8); 
	insertNode(root, 3);
	insertNode(root, 10);
	insertNode(root, 2);
	insertNode(root, 5);
	insertNode(root, 14);
	insertNode(root, 4);
	insertNode(root, 11);
	insertNode(root, 16); // insertNode함수를 이용해 과제에서 주어진 트리를 만들었습니다.

	printf("기준 노드를 입력하세요 : ");

	scanf("%d", &n); // 기준노드의 값을 입력받고

	root = searchtreeNode(root, n); // 기준노드를 루트노드로 다시 저장합니다.

	leftMax = maxNode(root)->data; // maxNode함수와
	rightMin = minNode(root)->data; // minNode함수를 이용해 값을 저장받습니다.
	
	printf("기준노드의  좌측서브트리에서  가장 큰 노드는 %d, 우측서브트리에서 가장 작은 노드는 %d 입니다\n", leftMax, rightMin);

	return 0;
}