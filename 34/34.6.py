class Node:
    def __init__(self, value: any):
        self.value: any = value
        self.next: Node = None


def solution(head: None) -> Node:
    if not head:
        return None
    A: Node = head
    B: Node = head.next
    head.next = None
    while B:
        C = B.next
        B.next = A
        A = B
        B = C
    return A


# RUNTIME: O(n), we iterate the LL once
#   SPACE: O(1), in place


def run_tests():

    def linked_list_to_array(head):
        result = []
        current = head
        while current:
            result.append(current.value)
            current = current.next
        return result

    def array_to_linked_list(arr):
        dummy_head = Node(0)
        current = dummy_head
        for val in arr:
            current.next = Node(val)
            current = current.next
        return dummy_head.next

    # Test cases
    tests = [
        # Test empty list
        ([], []),
        # Test single element list
        ([1], [1]),
        # Test multiple elements list
        ([1, 2, 3], [3, 2, 1]),
        # Test list with repeated values
        ([1, 1, 1], [1, 1, 1]),
        # Test list with negative values
        ([-1, -2, -3], [-3, -2, -1]),
        # Test list with zero
        ([0], [0]),
        # Test longer list
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
        # Test list with mixed values
        ([-1, 0, 1], [1, 0, -1]),
    ]

    for i, (arr, expected) in enumerate(tests):
        head = array_to_linked_list(arr)
        reversed_head = solution(head)
        got = linked_list_to_array(reversed_head)
        assert got == expected, f"\nTest {i + 1}: got: {got}, want: {expected}\n"
        print("PASS")


run_tests()
