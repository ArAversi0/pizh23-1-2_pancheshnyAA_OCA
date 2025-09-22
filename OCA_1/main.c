#include "sum_analysis.h"
#include <stdio.h>
#include <stdlib.h>
#include <windows.h>

int main(void) {
    SetConsoleOutputCP(CP_UTF8);
    
    calculate_sum(); // базовая задача

    size_t count = 0;
    int include_negative = 0;

    // Запрос у пользователя количества чисел
    printf("Введите количество чисел для генерации: ");
    if (scanf("%zu", &count) != 1 || count == 0) {
        printf("Некорректное значение. Используется 20 чисел по умолчанию.\n");
        count = 20;
    }

    // Запрос о необходимости отрицательных чисел
    printf("Включать отрицательные числа? (1 = да, 0 = нет): ");
    if (scanf("%d", &include_negative) != 1) {
        printf("Некорректное значение. Используется 0 (только положительные).\n");
        include_negative = 0;
    }

    // Генерация файла numbers.txt
    generate_numbers_file("numbers.txt", count, include_negative);

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
