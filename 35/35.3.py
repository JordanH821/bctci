class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def solution(head: Node) -> int:
    max_path: int = 0

    def helper(node: Node, depth: int) -> int:
        if not node:
            return 0
        left_path: int = helper(node.left, depth + 1)
        right_path: int = helper(node.right, depth + 1)
        if node.val == depth:
            # we can only take one path through the tree
            current_path = 1 + right_path + left_path
            nonlocal max_path
            # check if current path using this node and both subtrees is the max
            max_path = max(max_path, current_path)
            # bubble up the max path of the two subtrees and this node
            return 1 + max(left_path, right_path)
        else:
            return 0
    helper(head, 0)
    return max_path


# RUNTIME: O(n) we have to check every node
#   SPACE: O(h) where h is the height of the tree

def run_tests():
    tests = [
        # Test 1: Example from the book
        (
            Node(
                7,
                Node(1, Node(2, Node(4), Node(3)), Node(8)),
                Node(3, Node(2, Node(3), Node(3))),
            ),
            3,
        ),
        # Variation 1
        (
            Node(
                7,
                Node(1, Node(20, Node(4), Node(3)), Node(8)),
                Node(3, Node(2, Node(3), Node(3))),
            ),
            3,
        ),
        # Variation 2
        (
            Node(
                7,
                Node(1, Node(2, Node(4), Node(3)), Node(8)),
                Node(3, Node(20, Node(3), Node(3))),
            ),
            3,
        ),
        # Variation 3
        (
            Node(
                7,
                Node(1, Node(20, Node(4), Node(3)), Node(8)),
                Node(3, Node(20, Node(3), Node(3))),
            ),
            1,
        ),
        # Test 2: Empty tree
        (None, 0),
        # Test 3: Single aligned node
        (Node(0), 1),
        # Test 4: Single unaligned node
        (Node(1), 0),
        # Test 5: Path through root
        (Node(0, Node(1), Node(1)), 3),
        # Test 6: No aligned nodes
        (Node(5, Node(4), Node(2)), 0),
        # Test 7
        (Node(0, Node(1, Node(2), Node(2)), Node(1)), 4),
    ]

    for i, (root, want) in enumerate(tests, 1):
        got = solution(root)
        assert got == want, f"\naligned_path(): got: {got}, want: {want}\n"
        print("PASS", i)


run_tests()
