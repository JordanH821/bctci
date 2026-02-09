def solution(nested) -> int:
    def helper(lst, idx: int) -> int:
        if idx >= len(lst):
            return 0
        elif isinstance(lst[idx], list):
            return helper(lst[idx], 0) + helper(lst, idx + 1)
        else:
            return lst[idx] + helper(lst, idx + 1)

    return helper(nested, 0)

def solution2(arr) -> int:
    res = 0
    for elem in arr:
        if isinstance(elem, int):
            res += elem
        else:
            res += solution2(elem)
    return res

def run_tests():
    tests = [
        # Example 1 from book
        ([1, [2, 3], [4, [5]], 6], 21),
        # Example 2 from book
        ([[[[1]], 2]], 3),
        # Example 3 from book
        ([], 0),
        # Edge case - all nested single numbers
        ([[[[[1]]]]], 1),
        # Edge case - multiple empty arrays
        ([[], [], []], 0),
        # Edge case - mixed empty and non-empty arrays
        ([[], [1, 2], [], [3]], 6),
        # Edge case - deeply nested mixed arrays
        ([1, [2, [], [3, []], []], [4, [5, []]]], 15),
        # Edge case - all zeros
        ([0, [0, 0], [0, [0]], 0], 0),
        # Edge case - negative numbers
        ([-1, [-2, 3], [4, [-5]], 6], 5),
        # Stress test - large deeply nested array
        (
            [
                list(range(10)),
                [list(range(10, 20)), list(range(20, 30))],
                [list(range(30, 40)), [list(range(40, 50))]],
                list(range(50, 60)),
            ],
            sum(range(60)),
        ),
    ]
    # Test both implementations to verify they produce the same results
    for arr, want in tests:
        got = solution(arr)
        assert got == want, f"\nnested_array_sum({arr}): got: {got}, want: {want}\n"
        print("PASS")

        got = solution2(arr)
        assert got == want, f"\nnested_array_sum({arr}): got: {got}, want: {want}\n"
        print("PASS 2")


run_tests()
