class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def solution(node: Node, k: int) -> int:
    value: int = None
    curr: int = 0

    def helper(node):
        nonlocal curr
        nonlocal value
        if not node or value is not None:
            return
        helper(node.left)
        if curr == k:
            value = node.val
        curr += 1
        helper(node.right)

    helper(node)
    return value


# RUNTIME: O(n) we may need to touch every node
#   Space: O(h) for the BFS callstack


def run_tests():

    root = Node(5, Node(2, Node(1), Node(4)), Node(8, Node(6), Node(9)))

    tests = [
        (Node(5, Node(2, None, Node(4)), Node(9, Node(9), Node(11))), 4, 9),
        (Node(1), 0, 1),  # Single node
        (root, 0, 1),
        (root, 1, 2),
        (root, 2, 4),
        (root, 3, 5),
        (root, 4, 6),
        (root, 5, 8),
        (root, 6, 9),
    ]

    for root, k, want in tests:
        got = solution(root, k)
        assert got == want, f"\nkth_element(root, {k}): got: {got}, want: {want}\n"
        print("PASS")


run_tests()
