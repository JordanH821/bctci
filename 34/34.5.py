class Node:
    def __init__(self, value: any):
        self.value = value
        self.next = None

def solution(head: Node) -> Node:
    dummy_head = Node(None)
    dummy: Node = dummy_head
    curr: Node = head
    while curr:
        copy_node: Node = Node(curr.value)
        dummy.next = copy_node
        dummy = copy_node
        curr = curr.next
    return dummy_head.next


# RUNTIME: O(n) we have to iterate the entire list
#   SPACE: O(n) we return the entire list copied
def run_tests():

  def linked_list_to_array(head):
    result = []
    current = head
    while current:
      result.append(current.value)
      current = current.next
    return result

  def array_to_linked_list(arr):
    dummy = Node(0)
    current = dummy
    for val in arr:
      current.next = Node(val)
      current = current.next
    return dummy.next
  
  # Test cases
  tests = [
      # Test empty list
      [],
      # Test single element list
      [1],
      # Test multiple elements list
      [1, 2, 3],
      # Test list with repeated values
      [1, 1, 1],
      # Test list with negative values
      [-1, -2, -3],
      # Test list with zero
      [0],
      # Test longer list
      [1, 2, 3, 4, 5],
      # Test list with mixed values
      [-1, 0, 1],
  ]

  for i, arr in enumerate(tests):
    head = array_to_linked_list(arr)

    # Test second copy_list function
    copied_head_2 = solution(head)
    got_2 = linked_list_to_array(copied_head_2)
    assert got_2 == arr, f"\nTest {i + 1} (copy_list 2): got: {got_2}, want: {arr}\n"
    print("PASS")

run_tests()


