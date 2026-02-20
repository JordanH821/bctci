class Node:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def solution(node: Node) -> int:
    chain_max: int = 0
    def helper(node: Node, depth: int): 
        if not node:
            return 0
        left: int = helper(node.left, depth+1)
        right: int = helper(node.right, depth+1)
        if node.val != depth:
           nonlocal chain_max #### <---- nonlocal usage
           chain_max = max(left, right, chain_max)
           return 0
        else:
           return 1 + max(left, right)
    return max(helper(node, 0), chain_max)

# RUNTIME: O(n) where n is the number of nodes in the list
#   SPACE: O(h) because our recursion depth is down to the height of the tree

def run_tests():
  tests = [
      # Test 1: from the book
      (Node(7, Node(1, Node(2, Node(4), Node(3)),
                    Node(8)), Node(3, Node(2, Node(3)))), 3),
      # Test 2
      (Node(0,
            Node(1,
                 Node(2,
                      Node(3),
                      None),
                 Node(4)),
            Node(5)), 4),

      # Test 3: Empty tree
      (None, 0),

      # Test 4: Single node aligned at root
      (Node(0), 1),

      # Test 5: Single node not aligned
      (Node(1), 0),

      # Test 6: Multiple valid chains, should return longest
      (Node(0,
            Node(1,
                 Node(2,
                      Node(4),
                      None),
                 Node(2,
                      Node(3),
                      None))), 4),

      # Test 7: No aligned nodes
      (Node(5,
            Node(4,
                 Node(3),
                 Node(3)),
            Node(2)), 0),

      # Test 8
      (Node(0,
            Node(1),
            Node(1)), 2),
  ]

  for i, (root, want) in enumerate(tests, 1):
    got = solution(root)
    assert got == want, f"\nTest {i} failed! Got: {got}, Want: {want}"
    print("PASS")

run_tests()