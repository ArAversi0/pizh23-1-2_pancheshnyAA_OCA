#include "sum_analysis.h"
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

/* 
 * Реализует простую задачу: ввод двух чисел и вывод их суммы.
 */
void calculate_sum(void) { /* O(1) */
    long double a, b; /* O(1) - объявление переменных */
    
    printf("Введите первое число: "); /* O(1) - вывод строки */
    scanf("%Lf", &a); /* O(1) - ввод числа */
    
    printf("Введите второе число: "); /* O(1) - вывод строки */
    scanf("%Lf", &b); /* O(1) - ввод числа */
    
    long double result = a + b; /* O(1) - арифметическая операция */
    printf("Результат: %.10Lg\n", result); /* O(1) - вывод результата */
} /* Общая сложность: O(1) */

long double* read_numbers_from_file(const char* filename, size_t* count) { /* O(N) */
    FILE* file = fopen(filename, "r"); /* O(1) */
    if (!file) { /* O(1) */
        perror("Не удалось открыть файл"); /* O(1) */
        *count = 0; /* O(1) */
        return NULL; /* O(1) */
    }

    size_t capacity = 10; /* O(1) */
    size_t n = 0; /* O(1) */
    long double* numbers = malloc(capacity * sizeof(long double)); /* O(1) */
    if (!numbers) { /* O(1) */
        perror("Не удалось выделить память"); /* O(1) */
        fclose(file); /* O(1) */
        *count = 0; /* O(1) */
        return NULL; /* O(1) */
    }

    long double temp;
    size_t printed = 0;
    printf("Содержимое файла: "); /* O(1) */
    while (fscanf(file, "%Lf", &temp) == 1) { /* O(N) */
        if (n >= capacity) { /* O(1) */
            capacity *= 2; /* O(1) */
            numbers = realloc(numbers, capacity * sizeof(long double)); /* O(n) амортизированно O(N) */
        }
        numbers[n++] = temp; /* O(1) */

        if (printed < 20) { /* O(1) */
            printf("%.10Lg ", temp); /* O(1) */
            printed++; /* O(1) */
        }
    }

    if (n > 20) {
        printf("... (всего %zu чисел)\n", n); /* O(1) */
    } else {
        printf("\n"); /* O(1) */
    }

    fclose(file); /* O(1) */
    *count = n; /* O(1) */
    return numbers; /* O(1) */
} /* Общая сложность: O(N) */

/* sum_array
 * Вычисляет сумму всех элементов массива.
 * Сложность: O(N)
 */
long double sum_array(const long double* arr, size_t count) { /* O(1) */
    long double total = 0.0; /* O(1) - инициализация */
    for (size_t i = 0; i < count; i++) { /* O(N) - цикл по всем элементам */
        total += arr[i]; /* O(1) - сложение и присваивание */
    }
    return total; /* O(1) - возврат результата */
} /* Общая сложность: O(N) */

/* generate_numbers_file
 * Создаёт текстовый файл с указанным количеством чисел.
 * Параметры:
 *   filename - имя файла
 *   count - количество чисел
 *   include_negative - 1, если нужны отрицательные числа, 0 иначе
 * Сложность: O(N)
 */
void generate_numbers_file(const char* filename, size_t count, int include_negative) { /* O(1) */
    FILE* file = fopen(filename, "w"); /* O(1) */
    if (!file) { /* O(1) */
        perror("Не удалось создать файл"); /* O(1) */
        return; /* O(1) */
    }

    srand((unsigned int)time(NULL)); /* O(1) - инициализация генератора */

    for (size_t i = 0; i < count; i++) { /* O(N) */
        long double num = (rand() % 10000) / 100.0; /* O(1) - дробное число от 0 до 99.99 */
        if (include_negative && (rand() % 2 == 0)) { /* O(1) */
            num = -num; /* O(1) */
        }
        fprintf(file, "%.2Lf ", num); /* O(1) */
    }
    fprintf(file, "\n"); /* O(1) */

    fclose(file); /* O(1) */
} /* Общая сложность: O(N) */

