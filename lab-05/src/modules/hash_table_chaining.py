from typing import Any, List, Tuple, Optional
from hash_functions import HashFn, djb2, poly_hash, simple_hash

Bucket = List[Tuple[str, Any]]


class HashTableChaining:
    """
    Хеш-таблица на цепочках.

    Параметры:
        capacity: начальное число бакетов (будет >= 8).
        hash_fn: функция хеширования (signature: (key, mod) -> int).

    Время (ожидаемое):
        insert/get/remove: O(1) амортизированно (при разумном load factor).
    Память:
        O(n + m) где m — число бакетов.
    Устойчивость:
        операции с ключами не меняют порядок данных в бакете (зависит от контейнера).
    """
    def __init__(self, capacity: int = 8, hash_fn: HashFn = djb2):
        self._capacity = max(8, capacity)
        self._buckets: List[Bucket] = [[] for _ in range(self._capacity)]
        self._size = 0
        self._hash_fn = hash_fn

    def _index(self, key: str) -> int:
        """Вычисляет индекс бакета для ключа. O(1)."""
        return self._hash_fn(key, self._capacity)

    def insert(self, key: str, value: Any) -> None:
        """
        Вставляет пару (key, value) или обновляет значение, если ключ уже есть.
        Сложность: амортизированная O(1). При росте — O(n) на ресайз.
        """
        idx = self._index(key)
        bucket = self._buckets[idx]

        for i, (stored_key, _) in enumerate(bucket):
            if stored_key == key:
                bucket[i] = (key, value)
                return

        bucket.append((key, value))
        self._size += 1

        if self.load_factor() > 0.7:
            self._resize(self._capacity * 2)

    def get(self, key: str) -> Optional[Any]:
        """
        Возвращает значение по ключу или None, если ключа нет.
        Сложность: O(1 + alpha) где alpha — load factor.
        """
        idx = self._index(key)
        for stored_key, stored_value in self._buckets[idx]:
            if stored_key == key:
                return stored_value
        return None

    def remove(self, key: str) -> bool:
        """
        Удаляет ключ, если он существует. Возвращает True при успешном удалении.
        Сложность: O(1 + alpha).
        """
        idx = self._index(key)
        bucket = self._buckets[idx]

        for i, (stored_key, _) in enumerate(bucket):
            if stored_key == key:
                bucket.pop(i)
                self._size -= 1
                return True
        return False

    def contains(self, key: str) -> bool:
        """Проверка существования ключа. O(1 + alpha)."""
        return self.get(key) is not None

    def load_factor(self) -> float:
        """Текущий коэффициент заполнения: size / capacity."""
        return self._size / self._capacity

    def _resize(self, new_capacity: int) -> None:
        """
        Увеличение число бакетов и переразмеривание (rehash всех элементов).
        Сложность: O(n) при выполнении.
        """
        old_items: List[Tuple[str, Any]] = []

        for bucket in self._buckets:
            if bucket:
                old_items.extend(bucket)

        self._capacity = max(8, new_capacity)
        self._buckets = [[] for _ in range(self._capacity)]
        self._size = 0

        for key, value in old_items:
            self.insert(key, value)

    def __len__(self) -> int:
        return self._size


if __name__ == "__main__":
    table = HashTableChaining(hash_fn=poly_hash)
    table.insert("one", 1)
    table.insert("two", 2)

    print("one ->", table.get("one"))
    print("contains 'three' ->", table.contains("three"))
    print("load factor =", table.load_factor())
