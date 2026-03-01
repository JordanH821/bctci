from collections import deque


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def solution(root: Node) -> int:
    if not root:
        return -1
    queue = deque()
    queue.append((root, 0))
    levels: list[int] = []
    while queue:
        node, depth = queue.popleft()
        if not node:
            continue
        if depth >= len(levels):
            levels.append(0)
        levels[depth] += 1
        queue.append((node.left, depth + 1))
        queue.append((node.right, depth + 1))

    ret: int = 0
    average: float = 0.0
    for level_idx in range(len(levels) - 1):
        curr_avg = levels[level_idx + 1] / levels[level_idx]
        if curr_avg > average:
            average = curr_avg
            ret = level_idx
    return ret

# RUNTIME: O(n) touch every node
#   SPACE: O(n) we may store all nodes in the queue

def run_tests():
    # Test 1
    root1 = Node(5, Node(2, None, Node(6)), Node(9, Node(9, None, Node(1)), Node(8)))

    # Test 2: Empty tree
    root2 = None

    # Test 3: Single node
    root3 = Node(1)

    # Test 4: Perfect binary tree
    root4 = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))

    # Test 5: Unbalanced tree
    root5 = Node(1, Node(2, Node(4, Node(8), Node(9)), Node(5)), Node(3))

    # Test 6: Example from the book
    root6 = Node(1, Node(2, Node(4, Node(8), Node(9)), Node(5, None, Node(11))), None)
    # Test 7
    root7 = Node(1, Node(2, Node(4, Node(8), Node(9))))
    tests = [
        (root1, [0]),
        (root2, [-1]),  # Empty tree
        (root3, [0]),  # Single node: level 0 has prolificness 0
        # Level 0->1 and 1->2 both have prolificness 2
        (root4, [0, 1]),  # Both level 0 and 1 are valid answers
        (root5, [0]),
        (root6, [1]),
        (root7, [2]),
    ]

    for i, (root, valid_wants) in enumerate(tests):
        got = solution(root)
        assert (
            got in valid_wants
        ), f"\nmost_prolific_level(root{i + 1}): got: {got}, valid_wants: {valid_wants}\n"
        print("PASS")


run_tests()
