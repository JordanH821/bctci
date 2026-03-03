def solution(graph: list[list[int]], start, end) -> bool:
    visited: set[int] = set()
    visited.add(end)
    path: list[int] = []

    def visit(graph, node) -> bool:
        if node == start:
            # found the start so add it to path and return True so all ancestors are added
            path.append(node)
            return True
        else:
            for nbr in graph[node]:
                if nbr not in visited:
                    visited.add(nbr)
                    if visit(graph, nbr):
                        # if this path led to start add this node and return true
                        path.append(node)
                        return True
        return False

    # start at end so we do not have to reverse the list
    visit(graph, end)
    return path

# RUNTIME: O(V+E), we may end up touching every node
#   SPACE: O(V), the resulting path may contain every node
def run_tests():
    tests = [
        # Example 1 from book - graph from Figure 8
        [[[1], [0, 2, 5, 4], [1, 4, 5], [], [5, 2, 1], [1, 2, 4]], 0, 4, [0, 1, 4]],
        # Example 2 from book - graph from Figure 8, no path exists
        [[[1], [0, 2, 5, 4], [1, 4, 5], [], [5, 2, 1], [1, 2, 4]], 0, 3, []],
        # Simple line graph
        [[[1], [0, 2], [1]], 0, 2, [0, 1, 2]],
        # Cycle graph
        [[[1, 3], [0, 2], [1, 3], [0, 2]], 0, 2, [0, 1, 2]],
        # Disconnected graph
        [[[1], [0], [3], [2]], 0, 2, []],
        # Complete graph
        [[[1, 2], [0, 2], [0, 1]], 0, 2, [0, 2]],
    ]
    for graph, node1, node2, want in tests:
        got = solution(graph, node1, node2)
        # got_bfs = path_bfs(graph, node1, node2)
        # For this problem, there can be multiple valid paths
        # So we need to verify:
        # 1. If want is empty, got should be empty
        # 2. If want is not empty:
        #    - got should start with node1 and end with node2
        #    - got should be a valid path in the graph
        #    - got should not have duplicates
        if not want:
            assert (
                not got
            ), f"\npath({graph}, {node1}, {node2}): got: {got}, want empty path\n"
            #   assert not got_bfs, f"\npath_bfs({graph}, {node1}, {node2}): got: {got_bfs}, want empty path\n"
            continue

        assert (
            got[0] == node1 and got[-1] == node2
        ), f"\npath({graph}, {node1}, {node2}): path {got} should start with {node1} and end with {node2}\n"
        # assert got_bfs[0] == node1 and got_bfs[-1] == node2, f"\npath_bfs({graph}, {node1}, {node2}): path {got_bfs} should start with {node1} and end with {node2}\n"

        # Verify path is valid
        for i in range(len(got) - 1):
            assert (
                got[i + 1] in graph[got[i]]
            ), f"\npath({graph}, {node1}, {node2}): invalid path {got} - no edge between {got[i]} and {got[i + 1]}\n"
        # for i in range(len(got_bfs) - 1):
        #   assert got_bfs[i + 1] in graph[got_bfs[i]], \
        #       f"\npath_bfs({graph}, {node1}, {node2}): invalid path {
        #       got_bfs} - no edge between {got_bfs[i]} and {got_bfs[i + 1]}\n"

        # Verify no duplicates
        assert len(got) == len(
            set(got)
        ), f"\npath({graph}, {node1}, {node2}): path {got} contains duplicates\n"
        # assert len(got_bfs) == len(set(got_bfs)), \
        #     f"\npath_bfs({graph}, {node1}, {node2}): path {got_bfs} contains duplicates\n"
        print("PASS")


run_tests()
