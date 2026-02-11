class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head: Node = None
        self._size: int = 0

    def push_front(self, v) -> None:
        new_head: Node = Node(v)
        if self.head:
            new_head.next = self.head
            self.head = new_head
        else:
            self.head = new_head
        self._size += 1

    def pop_front(self):
        value = None
        if self.head:
            value = self.head.value
            self.head = self.head.next
            self._size -= 1
        return value

    def push_back(self, v):
        if not self.head:
            self.push_front(v)
        else:
            curr = self.head
            while curr and curr.next != None:
                curr = curr.next
            curr.next = Node(v)
            self._size += 1

    def pop_back(self):
        if self._size <= 1:
            return self.pop_front()
        prev = self.head
        next = self.head.next
        while next and next.next != None:
            tmp = next.next
            prev = next
            next = tmp
        prev.next = None
        self._size -= 1
        return next.value

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
    sll = SinglyLinkedList()

    # Test size on empty list
    assert sll.size() == 0, f"\nsize(): got: {sll.size()}, want: 0\n"

    # Test pop_front on empty list
    assert sll.pop_front() is None, "\npop_front() on empty list should return None\n"

    # Test pop_back on empty list
    assert sll.pop_back() is None, "\npop_back() on empty list should return None\n"

    # Test push_front and size
    sll.push_front(10)
    assert sll.size() == 1, f"\nsize(): got: {sll.size()}, want: 1\n"

    # Test push_back and size
    sll.push_back(20)
    assert sll.size() == 2, f"\nsize(): got: {sll.size()}, want: 2\n"

    # Test contains
    assert sll.contains(10) is not None, "\ncontains(10) should find the node\n"
    assert sll.contains(30) is None, "\ncontains(30) should not find the node\n"

    # Test pop_front
    assert sll.pop_front() == 10, "\npop_front() should return 10\n"
    assert sll.size() == 1, f"\nsize(): got: {sll.size()}, want: 1\n"

    # Test pop_back
    assert sll.pop_back() == 20, "\npop_back() should return 20\n"
    assert sll.size() == 0, f"\nsize(): got: {sll.size()}, want: 0\n"

    # Test push_back and pop_back
    sll.push_back(30)
    assert sll.pop_back() == 30, "\npop_back() should return 30\n"

    # Test push_front and pop_front
    sll.push_front(40)
    assert sll.pop_front() == 40, "\npop_front() should return 40\n"


run_tests()
