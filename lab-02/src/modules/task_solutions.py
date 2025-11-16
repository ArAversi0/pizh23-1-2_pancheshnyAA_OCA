from collections import deque


def check_brackets(s):
    """
    Проверка сбалансированности скобок.
    Используется стек на списке — операции push/pop O(1).
    Общая сложность: O(n).
    """
    stack = []  # O(1)

    for c in s:  # O(n)
        if c in "([{":           # O(1)
            stack.append(c)      # O(1)
        elif c in ")]}":         # O(1)
            if not stack:        # O(1)
                # Итоговая сложность функции check_brackets: O(n)
                return False     # O(1)

            top = stack.pop()    # O(1)

            if (c == ")" and top != "(") or \
               (c == "]" and top != "[") or \
               (c == "}" and top != "{"):   # O(1)
                # Итоговая сложность функции check_brackets: O(n)
                return False                # O(1)

    # Итоговая сложность функции check_brackets: O(n)
    return len(stack) == 0  # O(1)


def print_queue_simulation():
    """
    Симуляция работы очереди печати.
    deque обеспечивает операции push/pop O(1).
    """
    queue = deque()                  # O(1)
    queue.append("Документ1")        # O(1)
    queue.append("Документ2")        # O(1)
    queue.append("Документ3")        # O(1)

    print("=== Очередь печати ===")
    while queue:                     # O(n)
        print(f"Печатается: {queue.popleft()}")  # popleft — O(1)
    # Итоговая сложность функции print_queue_simulation: O(n)


def is_palindrome(s):
    """
    Проверка, является ли строка палиндромом.
    Используется deque, т.к. pop с обоих концов — O(1).
    Общая сложность: O(n).
    """
    dq = deque()  # O(1)

    for c in s:   # O(n)
        if c.isalnum():                    # O(1)
            dq.append(c.lower())           # O(1)

    while len(dq) > 1:                     # O(n)
        if dq.popleft() != dq.pop():       # каждая операция O(1)
            # Итоговая сложность функции is_palindrome: O(n)
            return False                   # O(1)

    # Итоговая сложность функции is_palindrome: O(n)
    return True  # O(1)
