#include "task_solutions.h"

// Проверка сбалансированности скобок с помощью стека
bool check_brackets(const std::string& s) {
    std::vector<char> stack;
    for (char c : s) {
        if (c == '(' || c == '[' || c == '{') stack.push_back(c);
        else if (c == ')' || c == ']' || c == '}') {
            if (stack.empty()) return false;
            char top = stack.back();
            stack.pop_back();
            if ((c == ')' && top != '(') ||
                (c == ']' && top != '[') ||
                (c == '}' && top != '{')) return false;
        }
    }
    return stack.empty();
}

// Симуляция очереди печати
void print_queue_simulation() {
    std::deque<std::string> queue;
    queue.push_back("Документ1");
    queue.push_back("Документ2");
    queue.push_back("Документ3");

    std::cout << "=== Очередь печати ===\n";
    while (!queue.empty()) {
        std::cout << "Печатается: " << queue.front() << std::endl;
        queue.pop_front();
    }
}

// Проверка палиндрома
bool is_palindrome(const std::string& s) {
    std::deque<char> dq;
    for (char c : s)
        if (std::isalnum(c))
            dq.push_back(std::tolower(c));

    while (dq.size() > 1) {
        if (dq.front() != dq.back()) return false;
        dq.pop_front();
        dq.pop_back();
    }
    return true;
}
