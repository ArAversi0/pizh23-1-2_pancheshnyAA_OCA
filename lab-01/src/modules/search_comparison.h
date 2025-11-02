#ifndef SEARCH_COMPARISON_H
#define SEARCH_COMPARISON_H

// Функция для вывода характеристик ПК
void print_pc_info(void);  // O(1)

// Функция линейного поиска
int linear_search(int arr[], int size, int target);  // O(n)

// Функция бинарного поиска (массив должен быть отсортирован)
int binary_search(int arr[], int size, int target);  // O(log n)

#endif