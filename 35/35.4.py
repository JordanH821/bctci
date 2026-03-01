class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def solution(node: Node) -> int:
    map = {}  # coordinates to count

    def helper(node, r, c) -> None:
        if not node:
            return
        if (r, c) not in map:
            map[(r, c)] = 0
        map[(r, c)] += 1
        helper(node.left, r + 1, c)
        helper(node.right, r, c + 1)

    helper(node, 0, 0)
    max_value: int = 0
    for value in map.values():
        max_value = max(max_value, value)
    return max_value


def run_tests():
    # Test 1: Example from the book - two nodes stacked
    root1 = Node(1)
    root1.left = Node(2)
    root1.right = Node(3)
    root1.left.left = Node(4)
    root1.left.right = Node(5)
    root1.left.left.right = Node(7)
    root1.right.left = Node(6)
    root1.right.left.left = Node(8)
    root1.right.left.right = Node(9)

    root2 = Node(1)

    root3 = Node(1, Node(2), Node(3))

    # Test 4: Perfect binary tree of depth 4
    root4 = Node(
        1,
        Node(
            2,
            Node(4, Node(8), Node(9, None, Node(16))),
            Node(5, Node(10, None, Node(17)), Node(11, Node(18), None)),
        ),
        Node(
            3,
            Node(6, Node(12), Node(13)),
            Node(7, Node(14, Node(19), None), Node(15, Node(20), None)),
        ),
    )

    tests = [
        (root1, 2),  # Example from book
        (root2, 1),  # Single node
        (root3, 1),
        (root4, 4),
    ]

    for i, (root, want) in enumerate(tests, 1):
        got = solution(root)
        assert got == want, f"\nmost_stacked(): got: {got}, want: {want}\n"
        print("PASS")


run_tests()
