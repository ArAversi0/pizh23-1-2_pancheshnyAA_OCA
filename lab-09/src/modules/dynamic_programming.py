"""
Модуль реализации алгоритмов динамического программирования.
Включает:
1. Числа Фибоначчи (3 подхода).
2. Задача о рюкзаке (0-1 Knapsack) + восстановление ответа.
3. НОП (LCS) + восстановление ответа.
4. Расстояние Левенштейна.
5. Практические задачи: LIS, Размен монет.
"""

# --- 1. Числа Фибоначчи ---

def fib_recursive(n):
    """
    Наивная рекурсия.
    """
    if n <= 1:  # O(1)
        return n
    # T(n-1) + T(n-2)
    return fib_recursive(n - 1) + fib_recursive(n - 2)
    # Временная сложность: O(2^n) - экспоненциальная.
    # Пространственная сложность: O(n) - стек вызовов.


def fib_memo(n, memo=None):
    """
    Нисходящее ДП (Top-Down) с мемоизацией.
    """
    if memo is None:  # O(1)
        memo = {}  # O(1)

    if n in memo:  # O(1) - поиск в хеш-таблице
        return memo[n]

    if n <= 1:  # O(1)
        return n

    # Вычисляем и сохраняем результат
    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)  # O(1)
    return memo[n]
    # Временная сложность: O(n).
    # Пространственная сложность: O(n).


def fib_tabulation(n):
    """
    Восходящее ДП (Bottom-Up) - табличный метод.
    """
    if n <= 1:  # O(1)
        return n

    dp = [0] * (n + 1)  # O(n)
    dp[1] = 1

    for i in range(2, n + 1):  # O(n)
        dp[i] = dp[i - 1] + dp[i - 2]  # O(1)

    return dp[n]
    # Временная сложность: O(n).
    # Пространственная сложность: O(n).


# --- 2. Задача о рюкзаке (0-1 Knapsack) ---

def knapsack_01(items, capacity, visualize=False):
    """
    Решает задачу о рюкзаке 0-1 методом восходящего ДП.
    items: список кортежей (weight, value).
    Возвращает: (max_value, selected_items).
    """
    n = len(items)  # O(1)

    dp = [[0] * (capacity + 1) for _ in range(n + 1)]  # O(n * W)

    # Заполнение таблицы
    for i in range(1, n + 1):  # O(n)
        weight, value = items[i - 1]  # O(1)
        for w in range(capacity + 1):  # O(W)
            if weight <= w:  # O(1)
                dp[i][w] = max(dp[i - 1][w], value + dp[i - 1][w - weight])  # O(1)
            else:
                dp[i][w] = dp[i - 1][w]  # O(1)

    if visualize:
        print("\nТаблица ДП для рюкзака:")
        for row in dp:
            print(row)

    # Восстановление ответа
    selected_items = []
    w = capacity
    for i in range(n, 0, -1):  # O(n)
        if dp[i][w] != dp[i - 1][w]:
            item = items[i - 1]
            selected_items.append(item)
            w -= item[0]

    return dp[n][capacity], selected_items
    # Временная сложность: O(n * W)
    # Пространственная: O(n * W)


# --- 3. НОП (LCS) ---

def lcs(s1, s2):
    """
    Находит длину LCS и саму подпоследовательность.
    """
    n, m = len(s1), len(s2)  # O(1)
    dp = [[0] * (m + 1) for _ in range(n + 1)]  # O(n * m)

    for i in range(1, n + 1):  # O(n)
        for j in range(1, m + 1):  # O(m)
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])  # O(1)

    # Восстановление ответа
    lcs_str = []
    i, j = n, m
    while i > 0 and j > 0:  # O(n + m)
        if s1[i - 1] == s2[j - 1]:
            lcs_str.append(s1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return dp[n][m], "".join(reversed(lcs_str))
    # Время: O(n * m)
    # Память: O(n * m)


# --- 4. Расстояние Левенштейна ---

def levenshtein_distance(s1, s2):
    """
    Вычисляет минимальное количество операций для превращения s1 в s2.
    """
    n, m = len(s1), len(s2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]  # O(n * m)

    for i in range(n + 1):  # O(n)
        dp[i][0] = i
    for j in range(m + 1):  # O(m)
        dp[0][j] = j

    for i in range(1, n + 1):  # O(n)
        for j in range(1, m + 1):  # O(m)
            cost = 0 if s1[i - 1] == s2[j - 1] else 1
            dp[i][j] = min(
                dp[i - 1][j] + 1,       # удаление
                dp[i][j - 1] + 1,       # вставка
                dp[i - 1][j - 1] + cost # замена
            )

    return dp[n][m]
    # Время: O(n * m)
    # Память: O(n * m)


# --- 5. Практические задачи ---

def coin_change(coins, amount):
    """
    Задача о размене монет (Минимальное количество монет).
    coins: доступные номиналы.
    amount: сумма.
    """
    dp = [float('inf')] * (amount + 1)  # O(A)
    dp[0] = 0

    for i in range(1, amount + 1):  # O(A)
        for coin in coins:  # O(C)
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1
    # Сложность: O(Amount * Coins)


def longest_increasing_subsequence(arr):
    """
    Задача LIS: Наибольшая возрастающая подпоследовательность.
    """
    if not arr:
        return 0

    n = len(arr)
    dp = [1] * n  # O(N)

    for i in range(1, n):  # O(N)
        for j in range(i):  # O(i)
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)  # O(N)
    # Сложность: O(N^2)
