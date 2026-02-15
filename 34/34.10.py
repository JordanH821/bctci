
class Node:
    def __init__(self, value: any):
        self.value = value
        self.next: Node = None

def solution(head: Node) -> any:
    slow: Node = head
    fast: Node = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow.value

# RUNTIME: O(n), we have to iterate the list
#   SPACE: O(1), no extra space

def run_tests():

  def array_to_linked_list(arr):
    head = Node(arr[0])
    current = head
    for val in arr[1:]:
      current.next = Node(val)
      current = current.next
    return head

  tests = [
      # Test single node
      ([10], 10),
      # Test two nodes
      ([10, 20], 20),
      # Test odd number of nodes
      ([10, 20, 30], 20),
      # Test even number of nodes
      ([10, 20, 30, 40], 30),
      # Test longer odd list
      ([10, 20, 30, 40, 50], 30),
      # Test longer even list
      ([10, 20, 30, 40, 50, 60], 40),
      # Test with negative values
      ([-10, -20, -30], -20),
      # Test with zeros
      ([0, 0, 0], 0),
  ]
  for i, (input_arr, want) in enumerate(tests):
    # Test the fast/slow pointer solution
    head = array_to_linked_list(input_arr)
    got = solution(head)
    assert got == want, f"\nTest {i + 1} (fast/slow): got: {got}, want: {want}\n"
    print("PASS")

run_tests()