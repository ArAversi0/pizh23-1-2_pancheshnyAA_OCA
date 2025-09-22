#include "sum_analysis.h"
#include <stdio.h>
#include <stdlib.h>
#include <windows.h>

int main(void) {
    SetConsoleOutputCP(CP_UTF8);
    
    calculate_sum(); // базовая задача

    size_t n = 0;
    long double* arr = read_numbers_from_file("numbers.txt", &n);
    if (arr) {
        printf("Всего считано %zu чисел из файла.\n", n);
        free(arr); // не забываем освобождать память
    }

    return 0;
}