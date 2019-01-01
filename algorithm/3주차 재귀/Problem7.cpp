#include <stdio.h>
#pragma warning(disable:4996)

int Scan(char *str, char target) {
	if (*str == '\0')
		return 0;
	if (*str == target)
		return 1 + Scan(str + 1, target);
	return Scan(str + 1, target);
}

int main() {
	char str[101];
	char c;
	scanf("%s%c%c", str, &c, &c);
	printf("%d\n", Scan(str, c));
	return 0;

}