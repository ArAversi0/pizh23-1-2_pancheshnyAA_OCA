#include <stdio.h>
#include <stdlib.h>
#include <locale.h>
#include "modules/search_comparison.h"

int main() { 
    // Вывод информации о компьютере
    print_pc_info();  // O(1)
    
    // Массив размеров для тестирования
    int sizes[] = {1000, 2000, 5000, 10000, 20000, 50000, 100000, 200000, 500000, 1000000};  // O(1)
    int num_sizes = sizeof(sizes) / sizeof(sizes[0]);  // O(1)
    int iterations = 100;  // O(1)
    int i;  // O(1)
    
    // Массивы для хранения времени выполнения
    double linear_times[num_sizes];   // O(1)
    double binary_times[num_sizes];   // O(1)

    printf("\nЗапуск сравнения алгоритмов поиска...\n");  // O(1)

    // Основной цикл тестирования
    for (i = 0; i < num_sizes; i++) {  // O(num_sizes)
        int size = sizes[i];  // O(1)
        printf("\nТестирование для размера массива: %d\n", size);  // O(1)
        
        // Генерация отсортированного массива
        int* arr = generate_sorted_array(size);  // O(n)
        if (arr == NULL) {
            printf("Ошибка выделения памяти для размера %d\n", size);
            continue;
        }

        // --- ТЕСТЫ ДЛЯ РАЗНЫХ ЦЕЛЕВЫХ ЭЛЕМЕНТОВ ---
        int targets[4];  // O(1)
        targets[0] = arr[0];           // Первый элемент
        targets[1] = arr[size - 1];    // Последний элемент
        targets[2] = arr[size / 2];    // Средний элемент
        targets[3] = -1;               // Отсутствующий элемент (заведомо не входит, т.к. массив содержит только чётные)

        const char* target_names[4] = {
            "первый элемент",
            "последний элемент",
            "средний элемент",
            "отсутствующий элемент"
        };

        double total_linear = 0.0;  // O(1)
        double total_binary = 0.0;  // O(1)

        // Проходим по каждому целевому элементу
        for (int t = 0; t < 4; t++) {  // O(4 * iterations * (n + log n))
            int target = targets[t];  // O(1)

            printf("Цель: %s\n", target_names[t]);  // O(1)

            double l_time = measure_time(linear_search, arr, size, target, iterations);  // O(iterations * n)
            double b_time = measure_time(binary_search, arr, size, target, iterations);  // O(iterations * log n)

            printf("Линейный поиск: %.9f сек\n", l_time);
            printf("Бинарный поиск: %.9f сек\n", b_time);
            printf("Отношение (линейный/бинарный): %.2f\n", l_time / b_time);

            total_linear += l_time;  // O(1)
            total_binary += b_time;  // O(1)
        }

        // Среднее время для данного размера массива по 4 типам целей
        linear_times[i] = total_linear / 4.0;  // O(1)
        binary_times[i] = total_binary / 4.0;  // O(1)

        free(arr);  // O(1)
    }

    // Запись результатов в CSV
    write_to_csv("C:/Users/user/Desktop/Passed/OCA/lab-01/src/data/search.csv",
         sizes, linear_times, binary_times, num_sizes);  // O(num_sizes)
    
    // Вывод теоретической информации
    printf("\nТеоретическая сложность алгоритмов:\n");
    printf("Линейный поиск: O(n)\n");
    printf("Бинарный поиск: O(log n)\n");
    printf("\nРезультаты сохранены в data/search_results.csv\n");

    return 0;  // O(1)
}

// Общая сложность программы: O(num_sizes * iterations * n)