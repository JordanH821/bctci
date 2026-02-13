class Node:
    def __init__(self, value):
        self.value = value
        self.prev: Node = None
        self.next: Node = None


class DoublyLinkedList:
    def __init__(self):
        self.head: Node = None
        self.tail: Node = None
        self._size: int = 0

    def push_front(self, v) -> None:
        new_head: Node = Node(v)
        if self.head:
            self.head.prev = new_head
            new_head.next = self.head
            self.head = new_head
        else:
            self.head = new_head
            self.tail = new_head
        self._size += 1

    def pop_front(self):
        value = None
        if self.head:
            value = self.head.value
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None
            self._size -= 1
        return value

    def push_back(self, v):
        if not self.head:
            self.push_front(v)
        else:
            new_node: Node = Node(v)
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            self._size += 1

    def pop_back(self):
        if self._size <= 1:
            return self.pop_front()
        value = self.tail.value
        self.tail = self.tail.prev
        self.tail.next = None
        self._size -= 1
        return value

    def size(self) -> int:
        return self._size

    def contains(self, v) -> bool:
        curr = self.head
        while curr:
            if curr.value == v:
                return curr
            curr = curr.next
        return None


def run_tests():
    dll = DoublyLinkedList()

    # Test size on empty list
    assert dll.size() == 0, f"\nsize(): got: {dll.size()}, want: 0\n"

    # Test pop_front on empty list
    assert dll.pop_front() is None, "\npop_front() on empty list should return None\n"

    # Test pop_back on empty list
    assert dll.pop_back() is None, "\npop_back() on empty list should return None\n"

    # Test push_front and size
    dll.push_front(10)
    assert dll.size() == 1, f"\nsize(): got: {dll.size()}, want: 1\n"

    # Test push_back and size
    dll.push_back(20)
    assert dll.size() == 2, f"\nsize(): got: {dll.size()}, want: 2\n"

    # Test contains
    assert dll.contains(10) is not None, "\ncontains(10) should find the node\n"
    assert dll.contains(30) is None, "\ncontains(30) should not find the node\n"

    # Test pop_front
    assert dll.pop_front() == 10, "\npop_front() should return 10\n"
    assert dll.size() == 1, f"\nsize(): got: {dll.size()}, want: 1\n"

    # Test pop_back
    assert dll.pop_back() == 20, "\npop_back() should return 20\n"
    assert dll.size() == 0, f"\nsize(): got: {dll.size()}, want: 0\n"

    # Test push_back and pop_back
    dll.push_back(30)
    assert dll.pop_back() == 30, "\npop_back() should return 30\n"

    # Test push_front and pop_front
    dll.push_front(40)
    assert dll.pop_front() == 40, "\npop_front() should return 40\n"


run_tests()
