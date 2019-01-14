#ifndef STRUCT_H
#define STRUCT_H

typedef struct info {
	char name[21];
	int price;
	int row, col;
}INFO;

typedef struct cinema {
	char name;
	int price;
	struct cinema *next;
}NODE;

typedef struct cinemaView {
	int cinema[8][8];
}VIEW;

#endif