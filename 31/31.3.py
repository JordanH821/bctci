def solution(nums: list[int], ops: list[int]):
    indices: list[int] = [i for i in range(len(nums))]
    # sort in place
    # sort tupes defaults to sorting by lowest index and then breaking ties with next index, so we should be good
    indices.sort(key=lambda i: nums[i])
    sorted_index: int = 0
    for op in ops:
        if op >= 0:
            nums[op] = None
        else:
            while sorted_index < len(nums) and nums[indices[sorted_index]] == None:
                sorted_index += 1
            nums[indices[sorted_index]] = None
    return [num for num in nums if num != None]


# RUNTIME: O(n log n + o) because we sorted the array and have to process o operations
# SPACE: O(n) because we duplicate the array and output up to the entire array if k is 0, sorting will also use O(n)


def run_tests():
    tests = [
        # Example 1 from the book
        ([50, 30, 70, 20, 80], [2, -1, 4, -1], [50]),
        # Example 2 from the book
        ([1, 2, 3], [], [1, 2, 3]),
        # Example 3 from the book
        ([1, 2, 3], [-1, -1, -1], []),
        # Edge case - delete all indices
        ([1, 2, 3], [0, 1, 2], []),
        # Edge case - single element
        ([1], [-1], []),
        # Edge case - duplicates
        ([5, 5, 5], [-1, -1], [5]),
        # Edge case - negative numbers
        ([-3, -2, -1], [-1, -1], [-1]),
        # Mixed operations with duplicates
        ([10, 10, 20, 20], [1, -1, -1], [20]),
        # Operations targeting same index
        ([1, 2, 3], [0, 0, 0], [2, 3]),
        # Alternating index and min operations
        ([5, 4, 3, 2, 1], [2, -1, 0, -1], [4]),
        # Large numbers within constraints
        ([10**9, -(10**9), 0], [-1, -1], [10**9]),
    ]
    for nums, operations, want in tests:
        got = solution(nums, operations)
        assert (
            got == want
        ), f"\nprocess_operations({nums}, {operations}): got: {got}, want: {want}\n"
        print("PASS")


run_tests()
