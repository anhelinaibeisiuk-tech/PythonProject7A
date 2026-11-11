

class Node:
    """Клас для представлення вузла (node), який зберігає дані та посилання на наступний вузол."""

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedQueue:
    """Черга на основі динамічно зв'язаних вузлів (Node-based Queue)."""

    def __init__(self):
        self.head = None  # Вказівник на початок черги
        self.tail = None  # Вказівник на кінець черги
        self._count = 0  # Лічильник кількості елементів

    def enqueue(self, item):
        """Додає новий елемент у кінець черги (Tail)."""
        new_node = Node(item)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._count += 1

    def dequeue(self):
        """Видаляє та повертає елемент з початку черги (Head) за правилом FIFO."""
        if self.head is None:
            print("Помилка: Черга порожня!")
            return None

        removed_data = self.head.data
        self.head = self.head.next

        if self.head is None:
            self.tail = None

        self._count -= 1
        return removed_data

    def size(self):
        """Повертає поточну кількість елементів у черзі."""
        return self._count

    def display(self):
        """Виводить усі елементи черги у порядку від Head до Tail."""
        if self.head is None:
            print("Черга порожня.")
            return

        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print("Черга (Head -> Tail): " + " -> ".join(elements))


# ==========================================
# 2. РЕАЛІЗАЦІЯ НА ОСНОВІ МАСИВУ
# ==========================================

class ArrayQueue:
    """Черга на основі масиву фіксованого розміру (Array-based Queue)."""

    def __init__(self, capacity=13):
        self.capacity = capacity
        self.array = [None] * capacity
        self.head = 0  # Індекс початку черги
        self.tail = 0  # Індекс кінця черги
        self._count = 0

    def enqueue(self, item):
        """Додає елемент у чергу."""
        if self._count == self.capacity:
            print("Помилка: Переповнення черги!")
            return False

        self.array[self.tail] = item
        self.tail = (self.tail + 1) % self.capacity
        self._count += 1
        return True

    def dequeue(self):
        """Видаляє та повертає елемент з початку черги."""
        if self._count == 0:
            print("Помилка: Черга порожня!")
            return None

        removed_data = self.array[self.head]
        self.array[self.head] = None
        self.head = (self.head + 1) % self.capacity
        self._count -= 1
        return removed_data

    def size(self):
        """Повертає кількість елементів у черзі."""
        return self._count

    def display(self):
        """Виводить вміст черги."""
        if self._count == 0:
            print("Черга порожня.")
            return

        elements = []
        idx = self.head
        for _ in range(self._count):
            elements.append(str(self.array[idx]))
            idx = (idx + 1) % self.capacity
        print("Черга (Масив): [" + ", ".join(elements) + "]")


# ==========================================
# 3. ПЕРЕВІРКА РОБОТИ ПРОГРАМИ
# ==========================================

if __name__ == "__main__":
    print("--- 1. ТЕСТУВАННЯ ЧЕРГИ НА ВУЗЛАХ (ПОСИЛАННЯХ) ---")
    queue_linked = LinkedQueue()

    # Додавання елементів (згідно з прикладом у методичці: 6, 4, 6, 2, 7)
    queue_linked.enqueue(6)
    queue_linked.enqueue(4)
    queue_linked.enqueue(6)
    queue_linked.enqueue(2)
    queue_linked.enqueue(7)

    queue_linked.display()
    print("Кількість елементів у черзі:", queue_linked.size())

    # Видалення двох перших елементів за правилом FIFO
    print("Видалено з черги:", queue_linked.dequeue())
    print("Видалено з черги:", queue_linked.dequeue())

    queue_linked.display()
    print("Поточна кількість елементів:", queue_linked.size())

    print("\n--- 2. ТЕСТУВАННЯ ЧЕРГИ НА МАСИВІ ---")
    queue_array = ArrayQueue(capacity=13)

    queue_array.enqueue(6)
    queue_array.enqueue(4)
    queue_array.enqueue(6)
    queue_array.enqueue(2)
    queue_array.enqueue(7)

    queue_array.display()
    print("Кількість елементів у черзі:", queue_array.size())

    print("Видалено з черги:", queue_array.dequeue())
    queue_array.display()
    print("Поточна кількість елементів:", queue_array.size())