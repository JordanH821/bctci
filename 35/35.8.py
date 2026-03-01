from collections import deque


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def solution(root: Node) -> list[Node]:
    result: list[Node] = []
    queue = deque()
    queue.append((root, 0))
    depth: int = 0
    while queue:
        node, ndepth = queue.popleft()
        if not node:
            # bypass null nodes
            continue
        # add children
        queue.append((node.left, ndepth + 1))
        queue.append((node.right, ndepth + 1))

        # append result if leftmost
        if depth == ndepth:
            depth += 1
            result.append(node.val)
    return result


# RUNTIME: O(n) we process every node
#   SPACE: O(n) we store the levels of the tree in a queue


def run_tests():

    # Test 1
    root1 = Node(1, Node(2, Node(4), Node(5)), Node(3, None, Node(6)))

    # Test 2: Empty tree
    root2 = None

    # Test 3: Single node
    root3 = Node(1)

    # Test 4: Only right children
    root4 = Node(1, None, Node(2, None, Node(3)))

    # Test 5: Only left children
    root5 = Node(1, Node(2, Node(3), None), None)

    # Test 6: Example from the book
    root6 = Node(5, Node(2, None, Node(6)), Node(9, Node(9, None, Node(1)), Node(8)))

    tests = [
        (root1, [1, 2, 4]),  # Example
        (root2, []),  # Empty tree
        (root3, [1]),  # Single node
        (root4, [1, 2, 3]),  # Only right children
        (root5, [1, 2, 3]),  # Only left children
        (root6, [5, 2, 6, 1]),  # Example from the book
    ]

    for i, (root, want) in enumerate(tests):
        got = solution(root)
        assert got == want, f"\nleft_view(root{i + 1}): got: {got}, want: {want}\n"
        print("PASS")


run_tests()
