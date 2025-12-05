import os
from typing import List, Optional, Tuple


def recursive_binary_search(arr: List[int], target: int, left: int, right: int) -> Optional[int]:
    """Рекурсивный бинарный поиск в отсортированном массиве arr[left:right+1].

    Временная сложность: O(log n)
    Пространственная сложность (стек): O(log n)
    """
    if left > right:  # O(1)
        return None

    mid = left + (right - left) // 2  # то же, просто альтернативная форма

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return recursive_binary_search(arr, target, mid + 1, right)
    else:
        return recursive_binary_search(arr, target, left, mid - 1)