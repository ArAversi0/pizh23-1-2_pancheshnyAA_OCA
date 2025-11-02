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
