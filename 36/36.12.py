from collections import deque


def solution(graph: list[list[int]], infected: list[int]) -> int:
    iteration = 0
    visited: set = set(infected)
    queue = deque()
    for i in infected:
        queue.append((i, 0))
    while len(visited) != len(graph):
        node, node_iteration = queue.popleft()
        iteration = node_iteration
        for nbr in graph[node]:
            if nbr not in visited:
                queue.append((nbr, iteration + 1))
        visited.add(node)
    return iteration


# RUNTIME: O(V+E)
#   SPACE: O(V)


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
            [0, 8, 17],  # infected
            3,
        ),
        ([[1, 2], [0, 2], [0, 1, 3], [2]], [0], 2),  # graph  # infected  # want
        # Single node graph
        ([[]], [0], 0),
        # Line graph
        ([[1], [0, 2], [1, 3], [2]], [0], 3),
        # Multiple initial infected nodes
        ([[1, 2], [0, 3], [0, 3], [1, 2]], [0, 3], 1),
    ]

    for graph, infected, want in tests:
        got = solution(graph, infected)
        assert (
            got == want
        ), f"\nall_infected({graph}, {infected}): got: {got}, want: {want}\n"
        print("PASS")


run_tests()
