class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def solution(node: Node) -> bool:
    prev: int = None

    def helper(node: Node) -> bool:
        nonlocal prev
        if not node:
            return False
        left = helper(node.left)
        curr = node.val == prev
        prev = node.val
        right = helper(node.right)
        return left or curr or right

    return helper(node)


# RUNTIME: O(n)
#  SPACE: O(h) BFS via recursion


def run_tests():
    # Example 1 - BST with duplicates
    root1 = Node(5, Node(2, None, Node(4)), Node(9, Node(9, None, Node(9)), Node(11)))

    # Example 2 - empty tree
    root2 = None

    # Example 3 - single node
    root3 = Node(1)

    # Example 4 - BST without duplicates
    root4 = Node(5, Node(2, Node(1), Node(4)), Node(8, Node(6), Node(9)))

    tests = [
        (root1, True),  # Has duplicates (9s)
        (root2, False),  # Empty tree has no duplicates
        (root3, False),  # Single node has no duplicates
        (root4, False),  # No duplicates
    ]

    for i, (root, want) in enumerate(tests):
        got = solution(root)
        assert got == want, f"\nhas_duplicate(root{i + 1}): got: {got}, want: {want}\n"
        print("PASS")


run_tests()
