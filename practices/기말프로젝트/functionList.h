#ifndef FUNC_H
#define FUNC_H

#pragma warning(disable:4996)
void initView(VIEW *in);
NODE* getNode();
void insertNODE(NODE** head, int i);
NODE* initCinema();
void printCinema(VIEW *view, NODE *head);
void reservation(VIEW *view, INFO *info, NODE *head, int *num);
void sortByName(INFO *info, int *n);
void printInfo(INFO *info, int *n);
void fileStore(VIEW *view, NODE *head, INFO *info, int *n);
void fileLoad(INFO *info, VIEW *view, int *n);
void deleteList(VIEW *view, INFO *info, int *n);

#endif