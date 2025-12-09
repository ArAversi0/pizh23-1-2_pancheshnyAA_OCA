"""
Модуль реализации жадных алгоритмов.
Включает:
1. Выбор заявок (Interval Scheduling).
2. Непрерывный рюкзак (Fractional Knapsack).
3. Кодирование Хаффмана (Huffman Coding).
"""
import heapq
from collections import Counter, namedtuple


# --- 1. Задача о выборе заявок (Interval Scheduling) ---

def interval_scheduling(intervals):
    """
    Выбирает максимальное количество непересекающихся интервалов.
    """
    # Сортируем по времени окончания (end)
    sorted_intervals = sorted(intervals, key=lambda x: x[1])  # O(N log N) - Timsort

    selected = []  # O(1) - создание списка
    last_finish_time = -1  # O(1) - инициализация

    # Перебор интервалов в порядке возрастания времени окончания
    for start, end in sorted_intervals:  # O(N)
        if start >= last_finish_time:  # O(1)
            selected.append((start, end))  # O(1)
            last_finish_time = end  # O(1)

    return selected  # O(1)
    # Общая сложность: O(N log N) + O(N) * O(1) = O(N log N)


# --- 2. Задача о непрерывном рюкзаке (Fractional Knapsack) ---

Item = namedtuple('Item', ['weight', 'value'])


def fractional_knapsack(items, capacity):
    """
    Решает задачу о непрерывном рюкзаке.
    """
    # Сортируем по удельной стоимости (v/w) по убыванию
    sorted_items = sorted(
        items,
        key=lambda obj: obj.value / obj.weight,
        reverse=True
    )  # O(N log N) - сортировка

    total_value = 0.0  # O(1)
    current_weight = 0.0  # O(1)
    fractions = []  # O(1)

    for item in sorted_items:  # O(N)
        if current_weight >= capacity:  # O(1)
            break

        if current_weight + item.weight <= capacity:  # O(1)
            current_weight += item.weight
            total_value += item.value
            fractions.append((item, 1.0))  # O(1)
        else:
            remain = capacity - current_weight  # O(1)
            fraction = remain / item.weight  # O(1)
            total_value += item.value * fraction  # O(1)
            fractions.append((item, fraction))  # O(1)
            current_weight = capacity  # O(1)
            break

    return total_value, fractions  # O(1)
    # Общая сложность: O(N log N) + O(N) = O(N log N)

