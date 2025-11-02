#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <errno.h>
#include <string.h>
#ifdef _WIN32
#include <windows.h>
#else
#include <time.h>
#endif
#include "search_comparison.h"

// Функция для вывода характеристик ПК
void print_pc_info(void) {
    printf("\nХарактеристики ПК для тестирования:\n"); // O(1)
    printf("- Процессор: Intel Core i5-12450H\n");     // O(1)
    printf("- Видеокарта: Nvidia RTX 4060 8GB 115W\n"); // O(1)
    printf("- ОЗУ: 16 GB DDR5\n");                     // O(1)
    printf("- Накопитель: SSD 1TB\n");                 // O(1)
    printf("- ОС: Windows 11 Pro\n");                  // O(1)
    printf("- Компилятор: GCC\n");                     // O(1)
}
// Общая сложность print_pc_info: O(1)

// Функция линейного поиска
int linear_search(int arr[], int size, int target) {
    int i;  // O(1) - объявление переменной
    // O(n) - проход по всем элементам массива
    for (i = 0; i < size; i++) {  // O(n) - цикл по n элементам
        if (arr[i] == target) {  // O(1) - сравнение
            return i;  // O(1) - возврат значения
        }
    }
    return -1;  // O(1) - возврат значения
}
// Общая сложность: O(n)

// Функция бинарного поиска (массив должен быть отсортирован)
int binary_search(int arr[], int size, int target) {
    int left = 0;  // O(1) - инициализация
    int right = size - 1;  // O(1) - инициализация
    int mid;  // O(1) - объявление переменной
    
    // O(log n) - на каждой итерации диапазон уменьшается вдвое
    while (left <= right) {  // O(log n) - цикл выполняется log?(n) раз
        mid = left + (right - left) / 2;  // O(1) - вычисление среднего
        
        if (arr[mid] == target) {  // O(1) - сравнение
            return mid;  // O(1) - возврат значения
        }
        else if (arr[mid] < target) {  // O(1) - сравнение
            left = mid + 1;  // O(1) - присваивание
        }
        else {  // O(1) - ветвление
            right = mid - 1;  // O(1) - присваивание
        }
    }
    return -1;  // O(1) - возврат значения
}
// Общая сложность: O(log n)

// Функция для генерации отсортированного массива
int* generate_sorted_array(int size) {
    int* arr = (int*)malloc(size * sizeof(int));  // O(n) - выделение памяти
    int i;  // O(1) - объявление переменной
    
    if (arr == NULL) {  // O(1) - проверка указателя
        return NULL;  // O(1) - возврат значения
    }
    
    // O(n) - заполнение массива
    for (i = 0; i < size; i++) {  // O(n) - цикл по n элементам
        arr[i] = i * 2;  // O(1) - присваивание (создание отсортированного массива)
    }
    
    return arr;  // O(1) - возврат указателя
}
// Общая сложность: O(n)

// Функция для измерения времени выполнения поиска
double measure_time(int (*search_func)(int[], int, int), int arr[], int size, int target, int iterations) {
    double total_time;  // O(1) - объявление переменной
    int i;  // O(1) - объявление переменной
    
    // Использование QueryPerformanceCounter для высокоточного измерения времени (аналог time.perf_counter() в Python)
    // Измеряем суммарное время всех итераций сразу для большей точности
    LARGE_INTEGER frequency, start, end;  // O(1) - объявление переменных
    QueryPerformanceFrequency(&frequency);  // O(1) - получение частоты счетчика
    
    // Измеряем время начала всех итераций
    QueryPerformanceCounter(&start);  // O(1) - получение времени начала всех итераций
    
    // O(iterations) - выполнение заданного количества итераций
    for (i = 0; i < iterations; i++) {  // O(iterations) - цикл
        search_func(arr, size, target);  // O(complexity) - вызов функции поиска
    }
    
    // Измеряем время окончания всех итераций
    QueryPerformanceCounter(&end);  // O(1) - получение времени окончания всех итераций
    
    // Вычисляем суммарное время и делим на количество итераций
    total_time = (double)(end.QuadPart - start.QuadPart) / frequency.QuadPart;  // O(1) - вычисление суммарного времени
  
    return total_time / iterations;  // O(1) - возврат среднего значения
}
// Общая сложность: O(iterations * complexity(search_func))

// Функция для записи результатов в CSV файл
void write_to_csv(const char* filename, int sizes[], double linear_times[], double binary_times[], int num_sizes) {
    FILE* file = fopen(filename, "w");  // O(1) - открытие файла
    int i;  // O(1) - объявление переменной
    
    if (file == NULL) {  // O(1) - проверка указателя
         printf("Ошибка открытия файла! Код errno = %d (%s)\n",
             errno, strerror(errno));  // O(1) - вывод сообщения
        return;  // O(1) - возврат
    }
    
    // Запись заголовка
    fprintf(file, "ArraySize,LinearSearchTime,BinarySearchTime\n");  // O(1) - запись в файл
    
    // O(num_sizes) - запись данных
    for (i = 0; i < num_sizes; i++) {  // O(num_sizes) - цикл
        fprintf(file, "%d,%.10f,%.10f\n", sizes[i], linear_times[i], binary_times[i]);  // O(1) - запись строки
    }
    
    fclose(file);  // O(1) - закрытие файла
    printf("Данные записаны в %s\n", filename);  // O(1) - вывод сообщения
}
// Общая сложность: O(num_sizes)