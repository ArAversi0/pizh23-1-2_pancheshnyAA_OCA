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

        long double total = sum_array(arr, n);
        printf("Сумма всех чисел: %.10Lg\n", total);

        free(arr); // освобождение памяти
    }

    return 0;
}
