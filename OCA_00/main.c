#include "sum_analysis.h"
#include <stdio.h>
#include <windows.h>

int main(void) {                // O(K * N)
    SetConsoleOutputCP(CP_UTF8);
    
    print_pc_info();                   // O(1)
    measure_execution_time();          // O(K * N)
    return 0;                          // O(1)
}
// Общая сложность main: O(K * N)