from typing import List

PC_INFO: str = (
    """
Характеристики ПК для тестирования:
- Процессор: Intel Core i5-12450H
- Оперативная память: 16 GB DDR4
- ОС: Windows 11 Pro
- Python: 3.10.9
"""
)


def is_sorted(arr: List[int]) -> bool:
    """Проверяет, что массив отсортирован по неубыванию.

    Сложность: O(n) по времени, O(1) по памяти.
    """
    # Используем более читаемую переменную для длины
    size = len(arr)
    return all(arr[i] <= arr[i + 1] for i in range(size - 1))


def bubble_sort(a: List[int]) -> List[int]:
    """Bubble Sort (пузырьковая сортировка), in-place.

    Best: O(n) (если реализована оптимизация с флагом swapped)
    Avg: O(n^2)
    Worst: O(n^2)
    Space: O(1)
    Устойчивость: устойчива
    """
    n = len(a)
    arr = a.copy()  # работаем с копией, чтобы не менять входной список (требование экспериментов)

    for i in range(n):
        swapped = False
        limit = n - i - 1
        for j in range(limit):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


def selection_sort(a: List[int]) -> List[int]:
    """Selection Sort (сортировка выбором), in-place.

    Best/Avg/Worst: O(n^2)
    Space: O(1)
    Устойчивость: неустойчива
    """
    arr = a.copy()
    n = len(arr)

    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr


def insertion_sort(a: List[int]) -> List[int]:
    """Insertion Sort (сортировка вставками), in-place.

    Best: O(n) (почти отсортированный)
    Avg: O(n^2)
    Worst: O(n^2)
    Space: O(1)
    Устойчивость: устойчива
    """
    arr = a.copy()
    size = len(arr)

    for i in range(1, size):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


def merge_sort(a: List[int]) -> List[int]:
    """Merge Sort (рекурсивный), возвращает новый отсортированный список.

    Best/Avg/Worst: O(n log n)
    Space: O(n) дополнительной памяти
    Устойчивость: устойчива
    """
    length = len(a)
    if length <= 1:
        return a.copy()

    mid = length // 2
    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])

    res: List[int] = []
    i = j = 0

    # Основной цикл слияния
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1

    # Добавляем оставшиеся элементы
    res.extend(left[i:])
    res.extend(right[j:])

    return res


def quick_sort(a: List[int]) -> List[int]:
    """Quick Sort (быстрая сортировка), некорректная in-place версия избегается ради ясности.

    Avg: O(n log n)
    Worst: O(n^2) (плохой выбор опорного)
    Space: O(log n) средняя глубина рекурсии + O(n).
    """
    if len(a) <= 1:
        return a.copy()

    pivot_index = len(a) // 2
    pivot = a[pivot_index]

    less = [x for x in a if x < pivot]
    equal = [x for x in a if x == pivot]
    greater = [x for x in a if x > pivot]

    return quick_sort(less) + equal + quick_sort(greater)


# Мапа алгоритмов
SORT_FUNCTIONS = {
    "bubble_sort": bubble_sort,
    "selection_sort": selection_sort,
    "insertion_sort": insertion_sort,
    "merge_sort": merge_sort,
    "quick_sort": quick_sort,
}
