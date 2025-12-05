from typing import Dict, Optional

PC_INFO: str = (
    "Характеристики ПК для тестирования:\n"
    "- CPU: (заполните)\n"
    "- RAM: (заполните)\n"
    "- ОС: (заполните)\n"
    "- Python: (заполните)\n"
)


def factorial(n: int) -> int:
    """Вычисляет факториал n рекурсивно.

    Базовый случай: factorial(0) == 1.
    Временная сложность: O(n) — выполняется n рекурсивных вызовов.
    Пространственная сложность (стек): O(n) — глубина рекурсии n.
    """
    if n < 0:
        raise ValueError("n must be non-negative")

    if n == 0:  # O(1)
        return 1

    # рекурсивный вызов + умножение
    return factorial(n - 1) * n  # то же, что n * factorial(...), порядок не влияет


def fib_naive(n: int) -> int:
    """Наивный рекурсивный расчёт n-го числа Фибоначчи.

    Определение:
        fib(0) = 0, fib(1) = 1
        fib(n) = fib(n-1) + fib(n-2) для n >= 2

    Временная сложность: O(phi^n) — экспоненциальная.
    Пространственная сложность (стек): O(n).
    """
    if n < 0:
        raise ValueError("n must be non-negative")

    if n < 2:  # O(1)
        return n

    # два независимых рекурсивных вызова
    left = fib_naive(n - 1)
    right = fib_naive(n - 2)
    return left + right