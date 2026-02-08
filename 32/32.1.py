def solution(arr: list[int]) -> list[int]:
    stack: list[int] = []
    for num in arr:
        if not stack or stack[-1] != num:
            stack.append(num)
        else:
            while stack and stack[-1] == num:
                num += stack.pop()
            stack.append(num)
    return stack

#RUNTIME: O(n), we loop thought the list, backtracking can only add a max of n across all runs so O(2n) -> O(n)
#SPACE: O(n), we may need to store the entire array in the stack if there are no consecutive duplicates


def run_tests():
    tests = [
        # Examples from problem description
        ([8, 4, 2, 2, 2, 4], [16, 2, 4]),
        ([4, 4, 4, 4], [16]),
        ([1, 2, 3, 4], [1, 2, 3, 4]),
        # Edge cases
        ([], []),
        ([1], [1]),
        ([0, 0], [0]),
        ([0, 0, 0, 0], [0]),
        # Multiple compression chains
        ([1, 1, 2, 2, 3, 3], [4, 2, 6]),
        ([2, 2, 2, 2, 2, 2], [8, 4]),
        # Alternating numbers
        ([1, 2, 1, 2, 1, 2], [1, 2, 1, 2, 1, 2]),
        # Numbers that sum to equal another number
        ([2, 2, 4], [8]),
        ([3, 3, 6, 6], [12, 6]),
        # Large numbers within constraints
        ([999, 999], [1998]),
        ([500, 500, 500, 500], [2000]),
        # Mix of different scenarios
        ([5, 5, 5, 1, 1, 5], [10, 5, 2, 5]),
    ]
    for arr, want in tests:
        got = solution(arr)
        assert got == want, f"\ncompress_array({arr}): got: {got}, want: {want}\n"
        print("PASS")


run_tests()
