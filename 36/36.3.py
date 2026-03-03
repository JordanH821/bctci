def solution(graph: list[list[int]]) -> bool:
    if not graph:
        return True
    visited: set[int] = set()

    def visit(graph, node):
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                visit(graph, neighbor)
    visit(graph, 0)
    edges = sum([len(neighbors) for neighbors in graph]) / 2
    # Acylic graphs have a most V-1 edges, so if it is connected and has V-1 edges it is acyclic. If it was not connected the number of edges cannot definitively determine if it is acyclic.
    return len(visited) == len(graph) and edges == len(graph) - 1


# RUNTIME: O(V+E), we need to touch every node
#   SPACE: O(V), we need to track the visited nodes


def run_tests():
    tests = [
        # Example 1 from the book
        ([[2], [2, 5], [0, 1, 3, 4], [2], [2], [1]], True),
        # Example 2 from the book
        ([[2], [5], [0, 3], [2], [], [1]], False),
        # Example 3 from the book
        ([[1], [0, 2, 5], [1, 3, 4], [2], [2, 5], [1, 4]], False),
        # Single node
        ([[]], True),
        # Two nodes connected
        ([[1], [0]], True),
        # Two nodes disconnected
        ([[], []], False),
        # Line graph (valid tree)
        ([[1], [0, 2], [1, 3], [2]], True),
        # Cycle
        ([[1, 3], [2, 0], [3, 1], [0, 2]], False),
        # Complete graph K4 (not a tree)
        ([[1, 2, 3], [0, 2, 3], [0, 1, 3], [0, 1, 2]], False),
        # Star graph
        ([[1, 2, 3, 4], [0], [0], [0], [0]], True),
    ]
    for graph, want in tests:
        got = solution(graph)
        assert got == want, f"\nis_tree({graph}): got: {got}, want: {want}\n"
        print("PASS")


run_tests()
