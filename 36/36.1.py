def solution(graph: list[list[int]]) -> bool:
    MIN_NODE: int = 0
    MAX_NODE: int = len(graph)-1
    sets: list[set] = [set() for _ in range(len(graph))]
    # Build sets of neighbors
    for vertex, neighbors in enumerate(graph):
        for neighbor in neighbors:
            # Validate requirements #1-3
            if neighbor in sets[vertex] or neighbor == vertex or neighbor < MIN_NODE or neighbor > MAX_NODE:
                return False
            sets[vertex].add(neighbor)

    # Validate requirement #4
    for vertex, neighbors in enumerate(graph):
        for neighbor in neighbors:
            if vertex not in sets[neighbor]:
                return False
    return True

# RUNTIME: O(V+E)
#   SPACE: O(V+E)
        
def run_tests():
  tests = [
      # Valid cases
      [[[1], [0]], True],  # Simple valid graph
      [[[1, 2], [0, 2], [0, 1]], True],  # Triangle graph
      [[], True],  # Empty graph
      [[[]], True],  # Single isolated node

      # Invalid node index cases
      [[[2], [0]], False],  # Node index too large
      [[[-1], []], False],  # Negative node index

      # Self-loop cases
      [[[0], []], False],  # Self loop
      [[[1], [1]], False],  # Self loop in second node

      # Parallel edge cases
      [[[1, 1], [0, 0]], False],  # Same edge twice from first node
      [[[1], [0, 2, 0], [1]], False],  # Same edge twice from second node

      # Unmatched edge cases
      [[[1], []], False],  # Edge only in one direction
      [[[1, 2], [0], []], False],  # Some edges missing their pairs
      [[[1], [2], [0]], False],  # Cycle with unmatched edges
  ]
  for graph, want in tests:
    got = solution(graph)
    assert got == want, f"\nvalidate({graph}): got: {got}, want: {want}\n"
    print("PASS")

run_tests()