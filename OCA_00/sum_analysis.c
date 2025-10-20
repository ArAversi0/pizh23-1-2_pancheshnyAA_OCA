#include "sum_analysis.h"
#include <stdio.h>      // O(1)
#include <stdlib.h>     // O(1)
#include <time.h>       // O(1)
#include <windows.h>    // O(1)

// ----------------------
// Вспомогательная функция для точного измерения времени
// ----------------------
double get_time_ms() {                               // O(1)
    LARGE_INTEGER freq, counter;                     // O(1)
    QueryPerformanceFrequency(&freq);                // O(1)
    QueryPerformanceCounter(&counter);               // O(1)
    return (double)counter.QuadPart * 1000.0 / (double)freq.QuadPart; // O(1)
}
// Общая сложность get_time_ms: O(1)


// ----------------------
// Простая задача: сумма двух чисел
// ----------------------
void calculate_sum(void) {                           // O(1)
    int a, b;                                        // O(1)
    printf("Введите два целых числа через пробел: "); // O(1)
    scanf("%d %d", &a, &b);                          // O(1)
    int result = a + b;                              // O(1)
    printf("Сумма: %d\n", result);                   // O(1)
}
// Общая сложность calculate_sum: O(1)


// ----------------------
// Генерация файла с числами
// ----------------------
void generate_numbers_file(const char *filename, size_t count, int allow_negative) { // O(N)
    FILE *file = fopen(filename, "w");               // O(1)
    if (!file) {                                     // O(1)
        perror("Ошибка при создании файла");         // O(1)
        return;                                      // O(1)
    }

    srand((unsigned)time(NULL));                     // O(1)
    for (size_t i = 0; i < count; i++) {             // O(N)
        int num = rand() % 1000;                     // O(1)
        if (allow_negative && rand() % 2 == 0) {     // O(1)
            num = -num;                              // O(1)
        }
        fprintf(file, "%d ", num);                   // O(1)
    }

    fclose(file);                                    // O(1)
}
// Общая сложность generate_numbers_file: O(N)


// ----------------------
// Чтение чисел из файла в массив
// ----------------------
double *read_numbers_from_file(const char *filename, size_t *out_count) { // O(N)
    FILE *file = fopen(filename, "r");             // O(1)
    if (!file) {                                   // O(1)
        perror("Ошибка открытия файла");           // O(1)
        return NULL;                               // O(1)
    }

    size_t capacity = 100;                         // O(1)
    double *numbers = malloc(capacity * sizeof(double)); // O(1)
    if (!numbers) {                                // O(1)
        perror("Ошибка выделения памяти");         // O(1)
        fclose(file);                              // O(1)
        return NULL;                               // O(1)
    }

    double num;                                    // O(1)
    size_t count = 0;                              // O(1)
    while (fscanf(file, "%lf", &num) == 1) {       // O(N)
        if (count >= capacity) {                   // O(1)
            capacity *= 2;                         // O(1)
            numbers = realloc(numbers, capacity * sizeof(double)); // O(1)
        }
        numbers[count++] = num;                    // O(1)
    }

    fclose(file);                                  // O(1)
    *out_count = count;                            // O(1)
    return numbers;                                // O(1)
}
// Общая сложность read_numbers_from_file: O(N)


// ----------------------
// Суммирование всех элементов массива
// ----------------------
double sum_array(const double *arr, size_t size) {  // O(N)
    double sum = 0.0;                               // O(1)
    for (size_t i = 0; i < size; i++) {             // O(N)
        sum += arr[i];                              // O(1)
    }
    return sum;                                     // O(1)
}
// Общая сложность sum_array: O(N)


// ----------------------
// Замер времени выполнения обеих функций
// ----------------------
void measure_execution_time(void) {                 // O(K * N)
    printf("\n=== Замер времени выполнения ===\n"); // O(1)

    // 1️⃣ Простая задача
    printf("\n[1] Простая задача (calculate_sum):\n"); // O(1)
    printf("Введите два числа для теста (например 10 20):\n"); // O(1)
    double start_simple = get_time_ms();            // O(1)
    calculate_sum();                                // O(1)
    double end_simple = get_time_ms();              // O(1)
    printf("Время выполнения (включая ввод): %.6f мс\n", end_simple - start_simple); // O(1)

    // 2️⃣ Усложнённая задача — суммирование массива из файла
    printf("\n[2] Суммирование массива из файла (sum_array):\n"); // O(1)
    size_t sizes[] = {1000, 5000, 10000, 50000, 100000}; // O(1)
    int num_sizes = sizeof(sizes) / sizeof(sizes[0]);     // O(1)

    for (int i = 0; i < num_sizes; i++) {                 // O(K)
        size_t n = sizes[i];                              // O(1)
        generate_numbers_file("numbers.txt", n, 1);       // O(N)
        size_t count;                                     // O(1)
        double *arr = read_numbers_from_file("numbers.txt", &count); // O(N)
        if (!arr) return;                                 // O(1)

        double start = get_time_ms();                     // O(1)
        double sum = sum_array(arr, count);               // O(N)
        double end = get_time_ms();                       // O(1)

        printf("Размер: %6zu | Сумма: %12.2f | Время: %10.6f мс\n", n, sum, end - start); // O(1)
        free(arr);                                        // O(1)
    }
}
// Общая сложность measure_execution_time: O(K * N)


// ----------------------
// Вывод характеристик ПК
// ----------------------
void print_pc_info(void) {                    // O(1)
    printf("\nХарактеристики ПК для тестирования:\n"); // O(1)
    printf("- Процессор: Intel Core i5-12450H\n");     // O(1)
    printf("- Видеокарта: Nvidia RTX 4060 8GB 115W\n"); // O(1)
    printf("- ОЗУ: 16 GB DDR5\n");                     // O(1)
    printf("- Накопитель: SSD 1TB\n");                 // O(1)
}
// Общая сложность print_pc_info: O(1)
