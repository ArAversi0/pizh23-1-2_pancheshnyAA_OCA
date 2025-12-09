import timeit
import copy
import csv
import os
from typing import List

from sorts_algs import SORT_FUNCTIONS, is_sorted, PC_INFO
from generate_data import generate_data


def measure_sort_time(func, data: List[int], runs: int = 3) -> float:
    """Возвращает среднее время в миллисекундах для func(copy(data))."""
    # использую более явное объявление функции вместо лямбды
    def stmt():
        return func(copy.deepcopy(data))

    total_time = timeit.timeit(stmt, number=runs)
    return (total_time / runs) * 1000.0


def run_experiments(
    sizes: List[int],
    data_types: List[str],
    runs: int = 3,
    csv_file: str = None
):
    results = []
    print(PC_INFO)

    # Автоматическое определение пути, если csv_file не передан
    if csv_file is None:
        # __file__ → .../lab-04/src/modules/<этот_файл>.py
        base_dir = os.path.dirname(__file__)            # .../lab-04/src/modules
        src_dir = os.path.dirname(base_dir)             # .../lab-04/src
        data_dir = os.path.join(src_dir, "data")        # .../lab-04/src/data
        os.makedirs(data_dir, exist_ok=True)
        csv_file = os.path.join(data_dir, "lab-04_results.csv")

    for data_type in data_types:
        for n in sizes:
            data = generate_data(n, data_type)

            for name, func in SORT_FUNCTIONS.items():

                # Пропускаем квадратичные для очень больших n ради практичности
                if n > 10000 and name in {"bubble_sort", "selection_sort", "insertion_sort"}:
                    print(f"Skipping {name} for n={n} (practical limit)")
                    continue

                t = measure_sort_time(func, data, runs=runs)

                # проверка корректности
                output = func(data.copy())
                assert is_sorted(output), (
                    f"{name} failed correctness for n={n}, type={data_type}"
                )

                results.append((name, n, data_type, t))
                print(f"{name:15} | type={data_type:12} | n={n:6} -> {t:8.3f} ms")

    # Сохранение CSV
    with open(csv_file, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["algorithm", "size", "data_type", "time_ms"])
        for algo, size, dtype, t in results:
            writer.writerow([algo, size, dtype, f"{t:.6f}"])

    print(f"Saved results to {csv_file}")
    return results


if __name__ == "__main__":
    # Примерные параметры
    sizes = [100, 500, 1000, 5000, 10000]
    data_types = ["random", "sorted", "reversed", "almost_sorted"]
    run_experiments(sizes, data_types, runs=3)
