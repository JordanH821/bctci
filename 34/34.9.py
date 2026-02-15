class Node:
    def __init__(self, value: any):
        self.value = value
        self.prev: Node = None
        self.next: Node = None


def solution(node: Node) -> list[any]:
    result: list[any] = []
    #find head
    curr: Node = node
    while curr.prev:
        curr = curr.prev
    # populate result
    while curr:
        result.append(curr.value)
        curr = curr.next
    return result
    
# RUNTIME: O(n) we need to get to the head and then iterate to the tail
#   SPACE: O(n) we need to accumulate all items in list

def run_tests():

  def create_doubly_linked_list(arr):
    head = Node(arr[0])
    cur = head
    for val in arr[1:]:
      new_node = Node(val)
      cur.next = new_node
      new_node.prev = cur
      cur = new_node
    return head


  def node_at_index(head, index):
    cur = head
    for _ in range(index):
      cur = cur.next
    return cur

  tests = [
      # Examples from the book
      ([1, 2, 3, 4], 2),
      ([1, 2, 3, 4], 0),

      ([1, 2, 3, 4, 5], 0),
      ([1, 2, 3, 4, 5], 1),
      ([1, 2, 3, 4, 5], 2),
      ([1, 2, 3, 4, 5], 3),
      ([1, 2, 3, 4, 5], 4),
      # Test single node
      ([1], 0),
  ]

  for i, (arr, index) in enumerate(tests):
    head = create_doubly_linked_list(arr)
    node = node_at_index(head, index)
    got = solution(node)
    assert got == arr, f"\nTest {i + 1}: got: {got}, want: {arr}\n"
    print("PASS")

run_tests()