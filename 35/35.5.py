class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def solution(node: Node) -> int:
    triangles: int = 0

    def helper(node, direction: str) -> int:
        if not node:
            return 0
        else:
            left = helper(node.left, "left")
            right = helper(node.right, "right")
            nonlocal triangles
            triangles += min(left, right)
            if direction == "left":
                return 1 + left
            else:
                return 1 + right

    helper(node, "left")
    return triangles

# RUNTIME: O(n), we have to touch every node
#   SPACE: O(h) the call stack for the tree traversal


def run_tests():
    tests = [
        # Example
        (Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7))), 4),
        (None, 0),  # Empty tree
        (Node(1), 0),  # Single node
        # No triangles - only left children
        (Node(1, Node(2, Node(3), None), None), 0),
        # No triangles - only right children
        (Node(1, None, Node(2, None, Node(3))), 0),
        (Node(1, Node(2), Node(3)), 1),
    ]

    for _, (root, want) in enumerate(tests):
        got = solution(root)
        assert got == want, f"\ntriangle_count(): got: {got}, want: {want}\n"
        print("PASS")


run_tests()
