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


@lru_cache(maxsize=None)
def fibonacci_memo(n: int) -> int:
    """
    Рекурсивная реализация Фибоначчи с мемоизацией (LRU-кеш).

    Сложность: время O(n), память O(n) (кеш + стек).
    """
    global call_count_memo
    call_count_memo += 1

    if n <= 1:
        return n

    return fibonacci_memo(n - 1) + fibonacci_memo(n - 2)


def measure_time(func: Callable[[int], int], n: int, runs: int = 1) -> float:
    """
    Возвращает среднее время выполнения func(n) в секундах.
    """
    cleaner = getattr(func, "cache_clear", None)
    if callable(cleaner):
        cleaner()

    timings: List[float] = []

    for _ in range(max(1, runs)):
        start = time.perf_counter()
        func(n)
        end = time.perf_counter()
        timings.append(end - start)

    return sum(timings) / len(timings)