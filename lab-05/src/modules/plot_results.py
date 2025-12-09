import random
import string
import matplotlib.pyplot as plt
from hash_table_chaining import HashTableChaining
from hash_table_open_addressing import HashTableOpenAddressing
from hash_functions import simple_hash, poly_hash, djb2
from performance import measure


def random_keys(n: int, length: int = 5) -> list[str]:
    """Генерация списка случайных строк-ключей."""
    chars = string.ascii_letters + string.digits
    return [''.join(random.choices(chars, k=length)) for _ in range(n)]


def analyze_collisions(hash_fn, n_elements: int = 500, capacity: int | None = None):
    """Возвращает список длин бакетов для анализа коллизий."""
    cap = capacity if capacity is not None else n_elements
    table = HashTableChaining(capacity=cap, hash_fn=hash_fn)

    keys = random_keys(n_elements)
    for idx, key in enumerate(keys):
        table.insert(key, idx)

    return [len(bucket) for bucket in table._buckets]


def plot_insert_time_vs_load():
    load_factors = [0.1, 0.5, 0.7, 0.9]
    chaining_times, open_times = [], []

    for lf in load_factors:
        t_insert, _, _ = measure(lambda: HashTableChaining(), n_ops=300, load=lf)
        chaining_times.append(t_insert)

        t_insert_oa, _, _ = measure(lambda: HashTableOpenAddressing(mode="linear"), n_ops=300, load=lf)
        open_times.append(t_insert_oa)

    plt.figure(figsize=(8, 5))
    plt.plot(load_factors, chaining_times, marker="o", label="Chaining insert")
    plt.plot(load_factors, open_times, marker="o", label="Open addressing insert")

    plt.xlabel("Load factor")
    plt.ylabel("Time (s)")
    plt.title("Insert time vs load factor")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()

    plt.savefig("lab05_insert_time.png")
    plt.show()
    print("Saved lab05_insert_time.png")


def plot_collision_histograms():
    funcs = [
        ("simple_hash", simple_hash),
        ("poly_hash", poly_hash),
        ("djb2", djb2),
    ]

    for name, fn in funcs:
        lengths = analyze_collisions(fn, n_elements=500)
        max_len = max(lengths)
        bins = range(0, max_len + 2)

        plt.figure(figsize=(8, 5))
        plt.hist(
            lengths,
            bins=bins,
            rwidth=0.9,
            align="left",
            color="skyblue",
            edgecolor="black",
        )

        plt.xlabel("Number of elements in bucket")
        plt.ylabel("Number of buckets")
        plt.title(f"Bucket size distribution — {name}")
        plt.yscale("log")
        plt.grid(True, which="both", linestyle="--", linewidth=0.5)
        plt.tight_layout()

        plt.savefig(f"collision_histogram_{name}.png")
        plt.show()
        print(f"Saved collision_histogram_{name}.png")


if __name__ == "__main__":
    plot_insert_time_vs_load()
    plot_collision_histograms()
