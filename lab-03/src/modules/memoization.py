import time
from functools import lru_cache
from typing import Callable, List, Tuple

import matplotlib.pyplot as plt


# Глобальные счётчики вызовов
call_count_naive: int = 0
call_count_memo: int = 0


def fibonacci_naive(n: int) -> int:
    """
    Наивная рекурсивная реализация Фибоначчи.

    Сложность: время O(phi^n), память (стек) O(n).
    """
    global call_count_naive
    call_count_naive += 1

    if n <= 1:
        return n

    # рекурсивный расчёт соседних значений
    a = fibonacci_naive(n - 1)
    b = fibonacci_naive(n - 2)
    return a + b