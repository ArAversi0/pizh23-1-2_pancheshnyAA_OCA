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


def hanoi_moves(n: int, src: str, aux: str, dst: str,
                moves: Optional[List[Tuple[str, str]]] = None) -> List[Tuple[str, str]]:
    """Генерирует последовательность перемещений для задачи Ханойских башен.

    Возвращает список кортежей (откуда, куда).

    Временная сложность: O(2^n) (количество перемещений = 2^n - 1).
    Пространственная сложность: O(n) (глубина рекурсии).
    """
    if moves is None:
        moves = []

    if n <= 0:
        return moves
    if n == 1:
        moves.append((src, dst))
        return moves

    # Перемещение n-1 дисков src -> aux
    hanoi_moves(n - 1, src, dst, aux, moves)

    # Перемещение самого большого диска
    moves.append((src, dst))

    # Перемещение n-1 дисков aux -> dst
    hanoi_moves(n - 1, aux, src, dst, moves)

    return moves