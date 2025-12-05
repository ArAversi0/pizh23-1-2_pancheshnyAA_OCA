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


def save_time_plot(ns: List[int], naive_times: List[float], memo_times: List[float], fname: str) -> None:
    """Строит и сохраняет график времени (сек)."""
    plt.figure(figsize=(8, 5))
    plt.plot(ns, naive_times, marker="o", label="Наивная рекурсия")
    plt.plot(ns, memo_times, marker="s", label="Мемоизация (lru_cache)")
    plt.title("Сравнение времени вычисления чисел Фибоначчи")
    plt.xlabel("n")
    plt.ylabel("Время (сек)")
    plt.grid(True, linestyle="--", linewidth=0.5)
    plt.legend()
    plt.savefig(fname, dpi=300, bbox_inches="tight")
    plt.show()
    plt.close()


def main() -> None:
    """Запускает эксперимент и сохраняет результаты."""
    ns: List[int] = list(range(5, 36, 5))

    naive_times: List[float] = []
    memo_times: List[float] = []
    naive_calls: List[int] = []
    memo_calls: List[int] = []

    for n in ns:
        global call_count_naive, call_count_memo
        call_count_naive = 0
        call_count_memo = 0

        # Наивная версия
        t_n = measure_time(fibonacci_naive, n, runs=1)
        naive_times.append(t_n)
        naive_calls.append(call_count_naive)

        # Мемоизация
        t_m = measure_time(fibonacci_memo, n, runs=3)
        memo_times.append(t_m)
        memo_calls.append(call_count_memo)

    # Таблица
    print(f"{'n':>3} | {'naive(s)':>10} | {'naive_calls':>11} | {'memo(s)':>10} | {'memo_calls':>10}")
    print("-" * 60)
    for i, n in enumerate(ns):
        print(
            f"{n:3d} | {naive_times[i]:10.6f} | {naive_calls[i]:11d} | "
            f"{memo_times[i]:10.6f} | {memo_calls[i]:10d}"
        )

    # График
    save_time_plot(ns, naive_times, memo_times, fname="fib_time_comparison.png")


if __name__ == "__main__":
    main()