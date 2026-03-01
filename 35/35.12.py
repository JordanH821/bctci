class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solution(node: Node, value: any) -> bool:
    if not node:
        return False
    if node.val == value:
        return True
    elif node.val < value:
        return solution(node.right, value)
    else:
        return solution(node.left, value)

# RUNTIME: O(log n)
#   SPACE: O(h)

def solution_iter(node: Node, value: any) -> bool:
    curr: Node = node
    while curr:
        if curr.val == value:
            return True
        curr = curr.right if curr.val < value else curr.left
    return False

# RUNTIME: O(log n)
#   SPACE: O(1)

def run_tests():
  # Test 1
  root1 = Node(5,
               Node(2,
                    None,
                    Node(4)),
               Node(9,
                    Node(9,
                         None,
                         Node(9)),
                    Node(11)))

  # Test 2: Empty tree
  root2 = None

  # Test 3: Single node
  root3 = Node(1)

  # Test 4: Perfect BST
  root4 = Node(4,
               Node(2,
                    Node(1),
                    Node(3)),
               Node(6,
                    Node(5),
                    Node(7)))

  # Test 5: Unbalanced BST
  root5 = Node(5,
               Node(3,
                    Node(2,
                         Node(1),
                         None),
                    Node(4)),
               None)

  tests = [
      (root1, 6, False),
      (root1, 9, True),
      (root1, 3, False),
      (root1, 4, True),
      (root2, 1, False),  # Empty tree
      (root3, 1, True),  # Single node, target exists
      (root3, 2, False),  # Single node, target doesn't exist
      (root4, 5, True),  # Perfect BST, target exists
      (root4, 8, False),  # Perfect BST, target doesn't exist
      (root5, 1, True),  # Unbalanced BST, target exists at leaf
      (root5, 5, True),  # Unbalanced BST, target exists at root
      (root5, 6, False),  # Unbalanced BST, target doesn't exist
  ]

  for i, (root, target, want) in enumerate(tests):
    got = solution(root, target)
    got = solution_iter(root, target)
    assert got == want, f"\nfind(root{i + 1}, {target}): got: {got}, want: {want}\n"
    print("PASS")

run_tests()