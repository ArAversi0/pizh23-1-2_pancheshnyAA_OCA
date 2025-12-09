"""
Модуль реализации структуры данных MinHeap (Куча).
"""
import math
import os  # добавлено: модуль может использоваться в составе src/modules


class MinHeap:
    """
    Реализация Min-Heap на основе динамического массива.
    Свойство кучи: значение в любом узле меньше или равно значениям его потомков.
    """

    def __init__(self):
        """Инициализация пустой кучи."""
        # Поддержка корректной работы при размещении в src/modules
        self.heap = []  # O(1) - создание пустого списка

    def _sift_up(self, index):
        """
        Всплытие элемента (sift-up).
        Поднимает элемент вверх, пока выполняется условие кучи.
        """
        while index > 0:  # O(log N) - в худшем случае проход от листа до корня
            parent_index = (index - 1) // 2  # O(1) - вычисление индекса родителя

            # Сравниваем элемент с родителем
            if self.heap[index] < self.heap[parent_index]:  # O(1) - сравнение
                # Меняем местами с родителем
                self.heap[index], self.heap[parent_index] = (
                    self.heap[parent_index],
                    self.heap[index],
                )  # O(1) - обмен элементов
                index = parent_index  # O(1) - переход на уровень выше
            else:
                break  # O(1) - условие кучи выполнено

    def _sift_down(self, index):
        """
        Погружение элемента (sift-down).
        Опускает элемент вниз, пока выполняется условие кучи.
        """
        size = len(self.heap)  # O(1)
        while True:  # O(log N) - в худшем случае спуск от корня до листа
            left_child = 2 * index + 1  # O(1)
            right_child = 2 * index + 2  # O(1)
            smallest = index  # O(1)

            # Проверяем левого потомка
            if (left_child < size and
                    self.heap[left_child] < self.heap[smallest]):  # O(1)
                smallest = left_child  # O(1)

            # Проверяем правого потомка
            if (right_child < size and
                    self.heap[right_child] < self.heap[smallest]):  # O(1)
                smallest = right_child  # O(1)

            # Если элемент больше одного из потомков, меняем местами
            if smallest != index:  # O(1)
                self.heap[index], self.heap[smallest] = (
                    self.heap[smallest],
                    self.heap[index],
                )  # O(1) - обмен
                index = smallest  # O(1) - переход на уровень ниже
            else:
                break  # O(1) - позиция найдена

   
