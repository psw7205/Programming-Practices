#include<stdio.h>
#include <stdlib.h>
#pragma warning(disable: 4996)

typedef struct {
	int degree;
	int *coef;
} poly; // 최대차수를 저장할 degree와 계수를 저장할 때 쓸 동적할당을 위한 포인터 coef입니다.

poly addpoly(poly a, poly b) // 두 다항식을 더하는 함수입니다.
{
	poly sum, max;
	int min = 0;

	if (a.degree > b.degree)
	{
		sum.degree = a.degree;
		min = b.degree;
		max = a;
	}
	else
	{
		sum.degree = b.degree; 
		min = a.degree;
		max = b;
	}
	// 큰 다항식의 계수는 sum으로, 더 작은 다항식은 min으로, 큰 다항식이 저장된 poly구조체는 max에 저장했습니다

	sum.coef = (int *)malloc(sizeof(int)*(sum.degree + 1)); // 더 큰 차수에 맞게 동적할당 하였습니다.

	for (int i = 0; i <= min; i++)
	{
		sum.coef[i] = a.coef[i] + b.coef[i];
	} // 오름차순으로 정리했기 때문에 순서대로 둘중 더 낮은 차수까지 더했습니다.
	for (int i = min+1; i <=sum.degree; i++)
	{
		sum.coef[i] = max.coef[i];
	}// 그 이후 차수부터는 더 큰 쪽만 저장합니다.
	 
	return sum;
}

int main()
{
	int a = 0, b = 0;
	poly c;
	poly d;
	poly sum;

	scanf("%d", &a);
	c.degree = a;
	c.coef = (int *)malloc(sizeof(int)*(a + 1));
	for (int i = 0; i <= a; i++)
	{
		scanf("%d", &c.coef[a - i]);
	}

	scanf("%d", &b);
	d.degree = b;
	d.coef = (int *)malloc(sizeof(int)*(b + 1));
	for (int i = 0; i <= b; i++)
	{
		scanf("%d", &d.coef[b - i]);
	} 
	
	// 다항식 a,b를 입력받고 역순(오름차순)으로 저장했습니다.

	sum = addpoly(c, d);

	for (int i = sum.degree; i >= 0; i--)
	{
		printf(" %d", sum.coef[i]);
	}

	free(c.coef);
	free(d.coef);
	free(sum.coef);
	return 0;
}
