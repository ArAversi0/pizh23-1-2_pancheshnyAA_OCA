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


# --- 3. Код Хаффмана (Huffman Coding) ---

class HuffmanNode:
    """Узел дерева Хаффмана."""
    def __init__(self, char, freq):
        self.char = char  # O(1)
        self.freq = freq  # O(1)
        self.left = None  # O(1)
        self.right = None  # O(1)

    def __lt__(self, other):
        return self.freq < other.freq  # O(1)


def build_huffman_tree(text):
    """
    Строит дерево Хаффмана.
    N - длина текста, K - количество уникальных символов (размер алфавита).
    """
    if not text:  # O(1)
        return None

    frequency = Counter(text)  # O(N)

    # Создание списка узлов
    heap = [HuffmanNode(ch, fr) for ch, fr in frequency.items()]  # O(K)
    heapq.heapify(heap)  # O(K)

    while len(heap) > 1:  # O(K)
        node1 = heapq.heappop(heap)  # O(log K)
        node2 = heapq.heappop(heap)  # O(log K)

        merged = HuffmanNode(None, node1.freq + node2.freq)
        merged.left = node1
        merged.right = node2

        heapq.heappush(heap, merged)  # O(log K)

    return heap[0]  # O(1)
    # Общая сложность: O(N) + O(K log K)


def generate_huffman_codes(node, prefix="", code_map=None):
    """
    Рекурсивный обход дерева для генерации кодов.
    K - количество узлов в дереве (2*unique_chars - 1).
    """
    if code_map is None:  # O(1)
        code_map = {}

    if node is not None:  # O(1)
        if node.char is not None:  # O(1)
            code_map[node.char] = prefix if prefix else "0"
        else:
            generate_huffman_codes(node.left, prefix + "0", code_map)
            generate_huffman_codes(node.right, prefix + "1", code_map)

    return code_map  # O(1)
    # Общая сложность: O(K)


def huffman_encoding(text):
    """Обертка для кодирования текста."""
    root = build_huffman_tree(text)  # O(N + K log K)
    codes = generate_huffman_codes(root)  # O(K)

    encoded_text = "".join(codes[ch] for ch in text)  # O(N)

    return encoded_text, codes, root
    # Общая сложность: O(N)