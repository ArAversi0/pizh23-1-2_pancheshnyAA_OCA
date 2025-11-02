from pathlib import Path  # O(1)
import pandas as pd       # O(1)
import matplotlib.pyplot as plt  # O(1)
import numpy as np  # O(1)

current_dir = Path(__file__).resolve().parent  # O(1) - получение директории текущего файла
data_path = current_dir.parent / "data" / "search.csv"  # O(1) - построение пути к CSV
report_path = Path("C:/Users/user/Desktop/Passed/OCA/lab-01/report")  # O(1) - путь к папке для сохранения графиков

# Создаём папку report, если её нет
report_path.mkdir(parents=True, exist_ok=True)  # O(1)

# Загружаем данные
try:
    df = pd.read_csv(data_path)  # O(n) - чтение CSV (n = число строк)
    print(f"Данные загружены из: {data_path}")  # O(1) - вывод сообщения
except FileNotFoundError:  # O(1)
    print(f"Файл не найден: {data_path}")  # O(1)
    exit(1)  # O(1)

# Основные переменные
sizes = df["ArraySize"]               # O(n) - извлечение колонки
linear_times = df["LinearSearchTime"] # O(n) - извлечение колонки
binary_times = df["BinarySearchTime"] # O(n) - извлечение колонки

# График 1: обычный масштаб
plt.figure(figsize=(10, 6))            # O(1) - создание фигуры
plt.plot(sizes, linear_times, marker='o', label="Линейный поиск")  # O(n) - построение линии
plt.plot(sizes, binary_times, marker='s', label="Бинарный поиск")  # O(n) - построение линии
plt.xlabel("Размер массива")           # O(1)
plt.ylabel("Время выполнения (сек)")  # O(1)
plt.title("Сравнение алгоритмов поиска")  # O(1)
plt.legend()                           # O(1)
plt.grid(True)                         # O(1)
plt.tight_layout()                      # O(1)
plt.savefig(report_path / "search_plot_linear.png")  # O(1) - сохранение графика
plt.close()                             # O(1) - закрытие фигуры

# График 2: логарифмический масштаб по оси y
plt.figure(figsize=(10, 6))            # O(1)
plt.plot(sizes, linear_times, marker='o', label="Линейный поиск")  # O(n)
plt.plot(sizes, binary_times, marker='s', label="Бинарный поиск")  # O(n)
plt.yscale("log")                       # O(1) - логарифмический масштаб по y
plt.xlabel("Размер массива")            # O(1)
plt.ylabel("Время выполнения (сек)")   # O(1)
plt.title("Сравнение алгоритмов поиска (логарифмический масштаб по y)")  # O(1)
plt.legend()                            # O(1)
plt.grid(True, which="both")            # O(1)
plt.tight_layout()                       # O(1)
plt.savefig(report_path / "search_plot_log.png")  # O(1) - сохранение графика
plt.close()                             # O(1)

# Теоретическая сложность (для сравнения)
# Линейный поиск: O(n)
# Бинарный поиск: O(log n)

# Вычисляем отношение времени линейного поиска к log(n) и бинарного поиска к log(n)
sizes_array = np.array(sizes)           # O(n)
linear_times_array = np.array(linear_times)  # O(n)
binary_times_array = np.array(binary_times)  # O(n)

# Проверяем, как растёт время относительно теории
linear_growth_ratio = linear_times_array / sizes_array         # O(n)
binary_growth_ratio = binary_times_array / np.log2(sizes_array) # O(n)

# Средние значения для оценки
mean_linear_ratio = np.mean(linear_growth_ratio)  # O(n)
mean_binary_ratio = np.mean(binary_growth_ratio)  # O(n)

print(f"Среднее время / O(n) для линейного поиска: {mean_linear_ratio:.2e}")  # O(1)
print(f"Среднее время / O(log n) для бинарного поиска: {mean_binary_ratio:.2e}")  # O(1)

# Интерпретация результатов
print("\nИнтерпретация:")
print("1. Линейный поиск растёт почти пропорционально размеру массива, что соответствует O(n).")
print("2. Бинарный поиск растёт очень медленно с увеличением размера массива, что соответствует O(log n).")
print("3. Расхождения могут быть вызваны:")
print("   - кешированием данных и особенностями работы ОС,")
print("   - случайными колебаниями времени выполнения в коротких интервалах.\n")