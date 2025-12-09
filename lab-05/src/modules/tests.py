"""
tests.py

Набор простых unit-тестов (не использует pytest, можно запускать напрямую).
Каждый тест возвращает True при успехе, в конце — сообщение.
"""

from hash_table_chaining import HashTableChaining
from hash_table_open_addressing import HashTableOpenAddressing


def test_chaining_basic() -> bool:
    table = HashTableChaining()
    table.insert("one", 1)
    table.insert("two", 2)

    assert table.get("one") == 1
    assert table.get("two") == 2
    assert table.get("three") is None
    assert table.contains("one")

    table.remove("one")
    assert not table.contains("one")
    return True


def test_open_addressing_basic() -> bool:
    table = HashTableOpenAddressing(mode="linear")
    table.insert("x", "X")
    table.insert("y", "Y")

    assert table.get("x") == "X"
    assert table.get("y") == "Y"
    assert table.contains("y")

    table.remove("x")
    assert not table.contains("x")
    return True


def test_collision_and_resize() -> bool:
    # проверяем, что после большого числа вставок — все элементы доступны
    table = HashTableChaining(capacity=4)
    for i in range(50):
        table.insert(f"k{i}", i)

    for i in range(50):
        assert table.get(f"k{i}") == i
    return True


if __name__ == "__main__":
    tests = [
        ("chaining_basic", test_chaining_basic),
        ("open_basic", test_open_addressing_basic),
        ("collision_resize", test_collision_and_resize),
    ]

    for name, test_fn in tests:
        try:
            ok = test_fn()
            print(f"{name}: OK" if ok else f"{name}: FAIL")
        except AssertionError as err:
            print(f"{name}: ASSERTION FAILED -> {err}")

    print("Тесты завершены")
