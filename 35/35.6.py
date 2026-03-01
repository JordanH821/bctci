class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def solution(node: Node) -> Node:
    if not node:
        return node
    tmp = node.left
    node.left = node.right
    node.right = tmp
    solution(node.left)
    solution(node.right)
    return node

# RUNTIME: O(n) we have to visit every node
#   SPACE: O(h) recusive call depth

def run_tests():

    # Test 1: Example from the book - tree with 4 triangles
    root1a = Node(
        1,
        Node(6, Node(4, None, Node(5)), Node(11)),
        Node(7, Node(2, None, Node(9)), None),
    )
    root1b = Node(1)
    root1b.left = Node(7)
    root1b.right = Node(6)
    root1b.left.right = Node(2)
    root1b.left.right.left = Node(9)
    root1b.right.left = Node(11)
    root1b.right.right = Node(4)
    root1b.right.right.left = Node(5)

    # Test 2: Empty tree
    root2 = None

    # Test 3: Single node
    root3 = Node(1)

    root4a = Node(1, Node(2, Node(3), None), None)
    root4b = Node(1, None, Node(2, None, Node(3)))

    tests = [
        (root1a, root1b),  # Example from book
        (root2, None),  # Empty tree
        (root3, root3),  # Single node
        (root4a, root4b),
    ]

    def same_values(t1, t2):
        if not t1 and not t2:
            return True
        if not t1 or not t2:
            return False
        return (
            t1.val == t2.val
            and same_values(t1.left, t2.left)
            and same_values(t1.right, t2.right)
        )

    for i, (root, want) in enumerate(tests, 1):
        got = solution(root)
        assert same_values(got, want), f"\ninvert(): got != want\n"
        print("PASS")


run_tests()
