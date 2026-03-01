import math


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def solution(node: Node) -> bool:
    def helper(node: Node, min_val: int, max_val: int) -> bool:
        if not node:
            return True
        if node.val < min_val or node.val > max_val:
            return False
        return helper(node.left, min_val, node.val) and helper(
            node.right, node.val, max_val
        )

    return helper(node, -math.inf, math.inf)


# RUNTIME: O(n) we have to check every node
#   SPACE: O(h)


def run_tests():
    # Example 1 - valid BST
    root1 = Node(5, Node(2, None, Node(4)), Node(9, Node(9, None, Node(9)), Node(11)))

    # Example 2 - empty tree
    root2 = None

    # Example 3 - single node
    root3 = Node(1)

    # Example 4 - invalid BST (right child smaller than parent)
    root4 = Node(5, Node(2), Node(4))

    # Example 5 - invalid BST (left child larger than parent)
    root5 = Node(5, Node(6), Node(7))

    tests = [
        (root1, True),  # Valid BST
        (root2, True),  # Empty tree is valid
        (root3, True),  # Single node is valid
        (root4, False),  # Invalid - right child smaller than parent
        (root5, False),  # Invalid - left child larger than parent
    ]

    for i, (root, want) in enumerate(tests):
        got = solution(root)
        assert got == want, f"\nis_bst(root{i + 1}): got: {got}, want: {want}\n"
        print("PASS")


run_tests()
