from collections import deque
import math


def BFS(graph: list[list[int]], node: int) -> dict[int, int]:
    distances: dict[int, int] = {node: 0}
    visited: set[int] = set()
    queue = deque()
    queue.append(node)
    while queue:
        node = queue.popleft()
        if node not in visited:
            for nbr in graph[node]:
                if nbr not in distances:
                    distances[nbr] = distances[node] + 1
                    queue.append(nbr)
            visited.add(node)
    return distances


def solution(graph: list[list[int]], n1, n2, n3) -> int:
    d1 = BFS(graph, n1)
    d2 = BFS(graph, n2)
    d3 = BFS(graph, n3)
    min_dist = math.inf
    for node in range(len(graph)):
        min_dist = min(d1[node] + d2[node] + d3[node], min_dist)
    return min_dist


# RUNTIME: O(3 * (V+E)) --> O(V+E)
#   SPACE: O(3 * V) --> O(V)


def run_tests():
    tests = [
        # Example from the book
        (
            [
                [1, 14],  # 0: Outer ring connections
                [0, 2],  # 1
                [1, 3],  # 2
                [2, 4],  # 3
                [3, 5, 19],  # 4: Connector from outer to inner ring
                [4, 6],  # 5
                [5, 7],  # 6
                [6, 8],  # 7
                [7, 9, 21],  # 8: Connector from outer to inner ring
                [8, 10],  # 9
                [9, 11],  # 10
                [10, 12],  # 11
                [11, 13],  # 12
                [12, 14],  # 13
                [0, 13, 15],  # 14: Connector from outer to inner ring
                [14, 16],  # 15
                [15, 17],  # 16
                [16, 18, 20],  # 17: Center node connections
                [17, 19],  # 18
                [18, 4],  # 19
                [17, 21],  # 20
                [8, 20],  # 21
            ],
            14,
            4,
            8,
            9,
        ),
        # Cycle with 5 nodes
        ([[1, 4], [0, 2], [1, 3], [2, 4], [0, 3]], 0, 2, 4, 3),
        # Simple line graph
        ([[1], [0, 2], [1]], 0, 1, 2, 2),
        # Star graph - optimal meeting point is center
        ([[1], [0, 2, 3, 4], [1], [1], [1]], 0, 2, 3, 3),
        # Complete graph - can meet at any node
        ([[1, 2, 3], [0, 2, 3], [0, 1, 3], [0, 1, 2]], 0, 1, 2, 2),
        # Edge case - all start at same node
        ([[1], [0]], 0, 0, 0, 0),
        # Edge case - two start at same node
        ([[1], [0, 2], [1]], 0, 0, 2, 2),
    ]
    for graph, node1, node2, node3, want in tests:
        got = solution(graph, node1, node2, node3)
        assert (
            got == want
        ), f"\nwalking_distance_to_coffee({graph}, {node1}, {node2}, {node3}): got: {got}, want: {want}\n"
        print("PASS")


run_tests()
