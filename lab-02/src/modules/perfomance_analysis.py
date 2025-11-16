import timeit  # O(1)
from collections import deque  # O(1)
import matplotlib.pyplot as plt  # O(1)
from linked_list import LinkedList  # O(1)


def plot_results(filename, sizes, times1, times2, label1, label2, title):
    """
    Построение графиков сравнения.
    Итоговая сложность: O(n)
    """
    plt.figure()  # O(1)
    plt.plot(sizes, times1, label=label1)  # O(n)
    plt.plot(sizes, times2, label=label2)  # O(n)

    plt.title(title)  # O(1)
    plt.xlabel("Размер списка")  # O(1)
    plt.ylabel("Время (сек)")  # O(1)
    plt.legend()  # O(1)

    plt.savefig("report/" + filename)  # O(n)
    plt.close()  # O(1)
    # Итоговая сложность функции: O(n)


def run_single_insert_test():
    """
    Выполняет практическое сравнение:
    - 1000 вставок в начало list → O(n)
    - 1000 вставок в начало LinkedList → O(1)
    Итоговая сложность: O(n)
    """

    ll = LinkedList()  # O(1)
    ll_time = timeit.timeit(
        stmt="for i in range(1000): ll.insert_at_start(i)",
        globals={"ll": ll},
        number=1
    )  # O(n)

    py_list = []  # O(1)
    list_time = timeit.timeit(
        stmt="for i in range(1000): py_list.insert(0, i)",
        globals={"py_list": py_list},
        number=1
    )  # O(n)

    print("\n=== Практическое сравнение вставки в начало (1000 операций) ===")
    print(f"LinkedList (O(1)):     {ll_time:.6f} сек")
    print(f"Python list (O(n)):    {list_time:.6f} сек")
    print("Теоретически: LinkedList O(1), list.insert(0) O(n)")
    
    # Вычисляем во сколько раз list медленнее LinkedList
    if ll_time > 0:
        ratio = list_time / ll_time
        if ratio >= 1:
            print(f"Разница: list оказался в {ratio:.1f} раз медленнее LinkedList на этой выборке")
        else:
            ratio = 1 / ratio
            print(f"Разница: list оказался в {ratio:.1f} раз быстрее LinkedList на этой выборке")

    # Итоговая сложность функции: O(n)


def run_single_queue_test():
    """
    Сравнение удаления из начала:
    - list.pop(0) — O(n)
    - deque.popleft() — O(1)
    1000 операций.
    Итоговая сложность: O(n)
    """

    lst = [0] * 1000  # O(n)
    dq = deque([0] * 1000)  # O(n)

    lst_time = timeit.timeit(
        stmt="for _ in range(1000): lst.pop(0)",
        globals={"lst": lst},
        number=1
    )  # O(n²)

    dq_time = timeit.timeit(
        stmt="for _ in range(1000): dq.popleft()",
        globals={"dq": dq},
        number=1
    )  # O(n)

    print("\n=== Практическое сравнение удаления из начала (1000 операций) ===")
    print(f"deque (O(1)):          {dq_time:.6f} сек")
    print(f"list pop(0) (O(n)):    {lst_time:.6f} сек")
    print("Теоретически: deque O(1), list.pop(0) O(n)")

    # Вычисляем во сколько раз list медленнее deque
    if dq_time > 0:
        ratio = lst_time / dq_time
        if ratio >= 1:
            print(f"Разница: list оказался в {ratio:.1f} раз медленнее deque на этой выборке")
        else:
            ratio = 1 / ratio
            print(f"Разница: list оказался в {ratio:.1f} раз быстрее deque на этой выборке")

    # Итоговая сложность: O(n)


# Графики

def compare_list_vs_linkedlist():
    """
    Строит графики для разных размеров входа.
    Итоговая сложность: O(sum N)
    """
    sizes = [1000, 2000, 5000, 10000, 20000]  # O(1)
    ll_times = []  # O(1)
    list_times = []  # O(1)

    for n in sizes:  # O(k)
        ll_time = timeit.timeit(
            stmt="for i in range(n): ll.insert_at_start(i)",
            setup="from linked_list import LinkedList; ll = LinkedList()",
            globals={"n": n},
            number=1
        )  # O(n)

        lst_time = timeit.timeit(
            stmt="for i in range(n): arr.insert(0, i)",
            setup="arr=[]",
            globals={"n": n},
            number=1
        )  # O(n²)

        ll_times.append(ll_time)  # O(1)
        list_times.append(lst_time)  # O(1)

    plot_results(
        "list_vs_linkedlist.png",
        sizes,
        ll_times,
        list_times,
        "LinkedList (O(1))",
        "list.insert(0) (O(n))",
        "Сравнение вставки в начало"
    )
    # Итоговая сложность: O(sum N)


def compare_list_vs_deque():
    """
    График удаления из начала list vs deque.
    Итоговая сложность: O(sum N)
    """
    sizes = [1000, 2000, 5000, 10000, 20000]  # O(1)
    deque_times = []  # O(1)
    list_times = []  # O(1)

    for n in sizes:  # O(k)
        dq_time = timeit.timeit(
            stmt="for _ in range(n): dq.popleft()",
            globals={"dq": deque([0] * n), "n": n},
            number=1
        )  # O(n)

        lst_time = timeit.timeit(
            stmt="for _ in range(n): arr.pop(0)",
            globals={"arr": [0] * n, "n": n},
            number=1
        )  # O(n²)

        deque_times.append(dq_time)  # O(1)
        list_times.append(lst_time)  # O(1)

    plot_results(
        "deque_vs_list.png",
        sizes,
        deque_times,
        list_times,
        "deque (O(1))",
        "list.pop(0) (O(n))",
        "Сравнение удаления из начала"
    )
    # Итоговая сложность: O(sum N)


if __name__ == "__main__":  # O(1)
    print("=== Старт анализа производительности ===")

    # Практические эксперименты
    run_single_insert_test()  # O(n)
    run_single_queue_test()  # O(n)

    # Построение графиков
    compare_list_vs_linkedlist()  # O(sum N)
    compare_list_vs_deque()  # O(sum N)

    print("\nГрафики сохранены, тесты завершены.")
