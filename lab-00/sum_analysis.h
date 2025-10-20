#ifndef SUM_ANALYSIS_H
#define SUM_ANALYSIS_H

#include <stddef.h>  // для size_t

// Простая задача: сумма двух чисел
void calculate_sum(void); // O(1)

// Генерация файла с числами
void generate_numbers_file(const char *filename, size_t count, int allow_negative); // O(N)

// Чтение чисел из файла
double *read_numbers_from_file(const char *filename, size_t *out_count); // O(N)

// Суммирование всех элементов массива
double sum_array(const double *arr, size_t size); // O(N)

// Измерение времени выполнения простой функции и функции суммирования массива
void measure_execution_time(void); // O(K * N)

// Вывод характеристик ПК
void print_pc_info(void); // O(1)

#endif