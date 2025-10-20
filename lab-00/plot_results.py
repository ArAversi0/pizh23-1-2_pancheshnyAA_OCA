import matplotlib.pyplot as plt
import pandas as pd

# Читаем результаты
data = pd.read_csv("c:/Users/user/Desktop/Выполненное/OCA/OCA_00/results.csv")

# Строим график
plt.figure(figsize=(8, 5))
plt.plot(data["N"], data["Time_ms"], marker="o")
plt.title("Зависимость времени выполнения от размера входных данных")
plt.xlabel("Размер массива N")
plt.ylabel("Время выполнения (мс)")
plt.grid(True)
plt.tight_layout()

# Сохраняем в файл
plt.savefig("plot.png")