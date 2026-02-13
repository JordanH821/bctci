class Node:
    def __init__(self, value: any):
        self.value: any = value
        self.next = None


def solution(head: Node, l: int, r: int) -> Node:
    if l == r:
        return head
    index: int = 0
    prev: Node = None
    curr: Node = head
    # iterate LL until we get to l
    while curr and index < l:
        prev = curr
        curr = curr.next
        index += 1

    # l > len(LL)
    if not curr:
        return head

    # keep track of the before node so we can point its next to the new head
    BEFORE: Node = prev
    TAIL_AFTER_REV: Node = curr
    # swap up to r or end of list
    while curr and index <= r:
        next: Node = curr.next
        curr.next = prev
        prev = curr
        curr = next
        index += 1

    # Point the new tail (BEFORE.next) to the AFTER section (curr or curr.next)
    # Either curr is None if we reach the end of the list of the first node out of the reverse window if not
    TAIL_AFTER_REV.next = curr
    if l == 0:
        return prev
    # handle BEFORE being None
    BEFORE.next = prev
    return head


def run_tests():

    def linked_list_to_array(head):
        result = []
        current = head
        while current:
            # print("HELLO", current.value)
            result.append(current.value)
            current = current.next
        return result

    def array_to_linked_list(arr):
        dummy = Node(0)
        current = dummy
        for val in arr:
            current.next = Node(val)
            current = current.next
        return dummy.next

    # Test cases
    tests = [
        # From book
        ([1, 2, 3, 4, 5], 1, 3, [1, 4, 3, 2, 5]),
        ([1, 2, 3, 4, 5], 2, 7, [1, 2, 5, 4, 3]),
        ([1, 2], 5, 6, [1, 2]),
        # Test empty list
        ([], 0, 1, []),
        # Test single element list
        ([1], 0, 1, [1]),
        # Test reversing entire list
        ([1, 2, 3], 0, 3, [3, 2, 1]),
        # Test reversing sublist with repeated values
        ([1, 1, 1, 2, 2], 1, 3, [1, 2, 1, 1, 2]),
        # Test reversing sublist with negative values
        ([-1, -2, -3, -4], 1, 3, [-1, -4, -3, -2]),
        # Test reversing sublist with zero
        ([0, 1, 2], 0, 1, [1, 0, 2]),
        # Test reversing sublist at the end
        ([1, 2, 3, 4, 5], 2, 4, [1, 2, 5, 4, 3]),
        # Test left beyond list length - should not modify
        ([1, 2, 3], 4, 5, [1, 2, 3]),
        # Test right beyond list length - reverse to end
        ([1, 2, 3], 1, 5, [1, 3, 2]),
    ]

    for i, (arr, left, right, expected) in enumerate(tests):
        head = array_to_linked_list(arr)
        reversed_head = solution(head, left, right)
        got = linked_list_to_array(reversed_head)
        assert got == expected, f"\nTest {i + 1}: got: {got}, want: {expected}\n"
        print("PASS")


run_tests()
