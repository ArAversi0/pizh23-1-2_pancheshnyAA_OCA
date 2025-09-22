#ifndef SUM_ANALYSIS_H
#define SUM_ANALYSIS_H

#include <stdlib.h>

/* Простая задача */
void calculate_sum(void); /* O(1) */

/* Чтение чисел из файла и вывод содержимого */
long double* read_numbers_from_file(const char* filename, size_t* count); /* O(N) */

#endif /* SUM_ANALYSIS_H */