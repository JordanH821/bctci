from collections import deque


def solution(graph: list[list[int]], start, queries) -> list[list[int]]:
    # First we build the BFS with predecessor tracking
    preds: dict = {start: None}
    visited: set = set()
    queue = deque()
    queue.append(0)
    while queue:
        node = queue.popleft()
        if node not in visited:
            for nbr in graph[node]:
                if nbr not in preds:
                    preds[nbr] = node
                    queue.append(nbr)
    print(preds, queue)
    # Find the path for each query
    paths: list[list[int]] = []
    for end in queries:
        if end not in preds:
            print("NOT IN PREDS", end, preds)
            paths.append([])
        else:
            path = []
            def helper(curr, stop):
                if curr == stop:
                    path.append(curr)
                    return
                helper(preds[curr], stop)
                path.append(curr)

            helper(end, start)
            paths.append(path)

    return paths

def run_tests():
  tests = [
      # Example
      [[[1], [0, 2, 5, 4], [1, 4, 5], [], [5, 2, 1], [1, 2, 4]], 0, [1, 0, 3, 4],
       [[0, 1], [0], [], [0, 1, 4]]],
      # Simple line graph
      [[[1], [0, 2], [1]], 0, [1, 2],
          [[0, 1], [0, 1, 2]]],
      # Disconnected components
      [[[1], [0], [3], [2]], 0, [1, 2, 3],
          [[0, 1], [], []]],
      # Complete graph
      [[[1, 2], [0, 2], [0, 1]], 0, [1, 2],
          [[0, 1], [0, 2]]],
      # Single node
      [[[]], 0, [0],
          [[0]]],
      # Empty queries
      [[[1], [0]], 0, [],
          []]
  ]
  for graph, start, queries, want in tests:
    got = solution(graph, start, queries)
    assert got == want, f"\nshortest_path_queries({graph}, {start}, {queries}): got: {got}, want: {want}\n"
    print("PASS")

run_tests()
