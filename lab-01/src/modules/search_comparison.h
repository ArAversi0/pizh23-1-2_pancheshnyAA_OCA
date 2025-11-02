#ifndef SEARCH_COMPARISON_H
#define SEARCH_COMPARISON_H

// Функция для вывода характеристик ПК
void print_pc_info(void);  // O(1)

// Функция линейного поиска
int linear_search(int arr[], int size, int target);  // O(n)

// Функция бинарного поиска (массив должен быть отсортирован)
int binary_search(int arr[], int size, int target);  // O(log n)

// Функция для генерации отсортированного массива
int* generate_sorted_array(int size);  // O(n)

// Функция для измерения времени выполнения поиска (использует QueryPerformanceCounter на Windows, clock_gettime на POSIX)
double measure_time(int (*search_func)(int[], int, int), int arr[], int size, int target, int iterations);  // O(iterations * complexity(search_func))

// Функция для записи результатов в CSV файл
void write_to_csv(const char* filename, int sizes[], double linear_times[], double binary_times[], int num_sizes);  // O(num_sizes)

#endif