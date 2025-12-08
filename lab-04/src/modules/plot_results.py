import csv
import matplotlib.pyplot as plt
from collections import defaultdict
import os


def load_csv(csv_file: str = "lab 04/src/lab04_results.csv"):
    data = defaultdict(list)
    with open(csv_file, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            alg = row["algorithm"]
            size = int(row["size"])
            dtype = row["data_type"]
            time_ms = float(row["time_ms"])
            data[alg].append((size, dtype, time_ms))
    return data



