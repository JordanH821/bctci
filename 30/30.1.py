def solution(connections) -> str:
    users: set[str] = set()
    for ip, username in connections:
        if username in users:
            return ip
        else:
            users.add(username)
    return ""


# RUNTIME: O(n*s) where n is the number of connections and s is the cost of hasing a string
# SPACE: O(n) since we store the set of usernames


def run_tests():
    tests = [
        # Example 1
        (
            [
                ("203.0.113.10", "mike"),
                ("298.51.100.25", "bob"),
                ("292.0.2.5", "mike"),
                ("203.0.113.15", "bob2"),
            ],
            ["203.0.113.10", "292.0.2.5"],
        ),
        # Example 2
        (
            [
                ("111.0.0.0", "mike"),
                ("111.0.0.1", "mike"),
                ("111.0.0.2", "bob"),
                ("111.0.0.3", "bob"),
            ],
            ["111.0.0.0", "111.0.0.1"],
        ),
        # Example 3
        (
            [
                ("111.0.0.0", "mike"),
                ("111.0.0.1", "mike2"),
                ("111.0.0.2", "mike3"),
                ("111.0.0.3", "mike4"),
            ],
            "",
        ),
        # Edge case - empty list
        ([], ""),
        # Edge case - single connection
        ([("1.1.1.1", "alice")], ""),
    ]
    for connections, want in tests:
        got = solution(connections)
        assert (
            got in want if isinstance(want, list) else got == want
        ), f"\naccount_sharing({connections}): got: {got}, want: {want}\n"
        print("PASS")


run_tests()
