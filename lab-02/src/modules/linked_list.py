class Node:
    """Узел связного списка. Создание занимает O(1)."""
    def __init__(self, value):
        self.value = value        # O(1)
        self.next = None          # O(1)


class LinkedList:
    """Односвязный список. Все операции указаны с оценками сложности."""

    def __init__(self):
        self.head = None          # O(1)
        self.tail = None          # O(1)
        # Итоговая сложность: O(1)

    def insert_at_start(self, value):
        """Вставка в начало списка — O(1)."""
        new_node = Node(value)    # O(1)
        new_node.next = self.head # O(1)
        self.head = new_node      # O(1)

        if self.tail is None:     # O(1)
            self.tail = new_node  # O(1)
        # Итоговая сложность метода insert_at_start: O(1)

    def insert_at_end(self, value):
        """Вставка в конец списка — O(1)."""
        new_node = Node(value)    # O(1)

        if self.head is None:     # O(1)
            self.head = new_node  # O(1)
            self.tail = new_node  # O(1)
            return                # O(1)

        self.tail.next = new_node # O(1)
        self.tail = new_node      # O(1)
        # Итоговая сложность метода insert_at_end: O(1)

    def delete_from_start(self):
        """Удаление из начала — O(1)."""
        if self.head is None:     # O(1)
            # Итоговая сложность метода delete_from_start: O(1)
            return                # O(1)

        self.head = self.head.next  # O(1)

        if self.head is None:       # O(1)
            self.tail = None        # O(1)
        # Итоговая сложность метода delete_from_start: O(1)

    def traversal(self):
        """Проход по всему списку — O(n)."""
        current = self.head
        while current is not None:           # O(n)
            print(current.value, end=" ")    # O(1)
            current = current.next           # O(1)
        print()                              # O(1)
        # Итоговая сложность метода traversal: O(n)
