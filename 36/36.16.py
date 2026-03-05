import math
from collections import deque


def get_distance(a1, a2, b1, b2) -> int:
    if b1 <= a1 <= b2 or b1 <= a2 <= b2 or a1 <= b1 <= a2 or a1 <= b2 <= a2:
        # overlap
        return 0
    return min([abs(a1 - b1), abs(a1 - b2), abs(a2 - b1), abs(a2 - b2)])


def solution(furniture, distance: int) -> bool:
    graph = [set() for _ in range(len(furniture))]
    for i in range(len(furniture)):
        for j in range(i + 1, len(furniture)):
            xi_min, yi_min, xi_max, yi_max = furniture[i]
            xj_min, yj_min, xj_max, yj_max = furniture[j]
            x_dist = get_distance(xi_min, xi_max, xj_min, xj_max)
            y_dist = get_distance(yi_min, yi_max, yj_min, yj_max)
            dist = math.sqrt(x_dist * x_dist + y_dist * y_dist)
            if dist <= distance:
                graph[i].add(j)
                graph[j].add(i)

    visited = set()
    visited.add(0)

    def visit(node):
        for nbr in graph[node]:
            if nbr not in visited:
                visited.add(nbr)
                visit(nbr)

    visit(0)
    return len(furniture) - 1 in visited

def run_tests():
  tests = [
      # Example 1 from the book:
      [[[1, 1, 9, 5],
        [12, 9, 20, 13],
        [16, 2, 22, 7],
        [24, 9, 26, 11],
        [29, 1, 31, 5]], 5, True],
      # Example 2 from the book:
      [[[1, 1, 9, 5],
        [12, 9, 20, 13],
        [16, 2, 22, 7],
        [24, 9, 26, 11],
        [29, 1, 31, 5]], 4, False],

      [[[0, 0, 1, 1], [1, 1, 2, 2], [2, 2, 3, 3], [3, 3, 4, 4], [4, 4, 5, 5]], 0, True],
      [[[0, 0, 1, 1], [1, 1, 2, 2], [2, 2, 3, 3], [3, 3, 4, 4], [4, 4, 5, 5]], 1, True],
      [[[0, 0, 1, 1], [1, 1, 2, 2], [3, 3, 4, 4], [4, 4, 5, 5]], 1, False],
      [[[0, 0, 1, 1], [1, 1, 2, 2], [3, 3, 4, 4], [4, 4, 5, 5]], 2, True],
      # Single piece of furniture
      [[[0, 0, 1, 1]], 5, True],
      # Two pieces far apart
      [[[0, 0, 1, 1], [10, 10, 11, 11]], 5, False],
      # Two pieces just within reach
      [[[0, 0, 1, 1], [5, 5, 6, 6]], 5.7, True],
      # Two pieces just out of reach
      [[[0, 0, 1, 1], [5, 5, 6, 6]], 5.6, False],
      # Pieces in a line
      [[[0, 0, 1, 1], [1, 0, 2, 1], [2, 0, 3, 1]], 1.5, True],
  ]
  for furniture, d, want in tests:
    got = solution(furniture, d)
    assert got == want, f"\ncan_reach({furniture}, {d}): got: {got}, want: {want}\n"
    print("PASS")

run_tests()