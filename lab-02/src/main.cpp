#include <iostream>
#include "modules/linked_list.h"
#include "modules/perfomance_analysis.h"
#include "modules/task_solutions.h"

int main() {
    std::cout << "===== Демонстрация LinkedList =====\n";
    LinkedList list;
    list.insert_at_end(1);
    list.insert_at_end(2);
    list.insert_at_start(0);
    list.traversal();
    list.delete_from_start();
    list.traversal();

    std::cout << "\n===== Анализ производительности =====\n";
    compare_list_vs_linkedlist();
    compare_list_vs_deque();
    std::cout << "Графики сохранены в папку report/\n";

    std::cout << "\n===== Решение задач =====\n";

    std::string s = "{[()]}";
    std::cout << "Сбалансированные скобки (" << s << "): "
              << (check_brackets(s) ? "OK" : "Ошибка") << std::endl;

    print_queue_simulation();

    std::string p = "A man a plan a canal Panama";
    std::cout << "Палиндром '" << p << "': "
              << (is_palindrome(p) ? "Да" : "Нет") << std::endl;

    return 0;
}
