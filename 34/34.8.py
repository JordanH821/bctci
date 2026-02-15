class Node:
    def __init__(self, value: any):
        self.value: any = value
        self.next: Node = None

def solution(head: Node) -> bool:
    if not head.next:
        return False
    slow: Node = head
    fast: Node = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            return True
    return False

# RUNTIME: O(n): we will have to loop over the entire list to find the cycle
#   SPACE: O(1): no extra space

def run_tests():

  # arr: non-empty array representing the linked list
  # final_pointer_index: index of the node that the last pointer's next pointer
  # should point to.
  # If final_pointer_index is -1, then the last pointer's next pointer should
  # point to null.
  #
  # Returns the head of the list
  def create_cyclic_list(arr, final_pointer_index):

    # Build list and store cycle start node
    dummy_head = Node(0)
    current = dummy_head
    cycle_start_node = None
    for i, val in enumerate(arr):
      current.next = Node(val)
      current = current.next
      if i == final_pointer_index:
        cycle_start_node = current

    # Create cycle if needed
    if cycle_start_node:
      current.next = cycle_start_node

    return dummy_head.next

  tests = [
      # Test: (list, final_pointer_index, want)

      # Single node no cycle
      ([1], -1, False),
      # Single node with cycle
      ([1], 0, True),
      # Multiple nodes with no cycle
      ([1, 2, 3, 4, 5], -1, False),
      # Multiple nodes all in a cycle
      ([1, 2, 3, 4, 5], 0, True),
      # Multiple nodes with cycle in the middle
      ([1, 2, 3, 4, 5], 2, True),
      # Multiple nodes with cycle at the end
      ([1, 2, 3, 4, 5], 4, True),
      # The length of the cycle is equal to the distance from the
      # head to the start of the cycle (both are 5)
      ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5, True),
      # The length of the cycle is greater than the distance from the
      # head to the start of the cycle
      ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 4, True),
      # The length of the cycle is less than the distance from the
      # head to the start of the cycle
      ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 6, True),
  ]

  for i, (arr, final_pointer_index, want) in enumerate(tests):
    head = create_cyclic_list(arr, final_pointer_index)
    got = solution(head)

    if final_pointer_index == -1:
      cycle_desc = "no cycle"
    else:
      cycle_desc = f"cycle starting at index {final_pointer_index}"
    test_case_str = f"Test {i + 1}: has_cycle(list {arr} with {cycle_desc})"
    assert got == want, f"\n{test_case_str}: got: {got}, want: {want}"
    print("PASS")

run_tests()