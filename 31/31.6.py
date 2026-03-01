def solution(nums: list[int], k: int):
    nums.sort()
    return nums[:k]

# RUNTIME: O(nlogn), for sorting
#   SPACE: O(n), sorting space

def run_tests():
  tests = [
      # Example from the book
      ([15, 4, 13, 8, 10, 5, 2, 20, 3, 9, 11, 27], 5, [2, 3, 4, 5, 8]),
      # Edge case - k = 1
      ([5, 2, 1, 3, 4], 1, [1]),
      # Edge case - k = length of array
      ([3, 1, 2], 3, [1, 2, 3]),
      # Edge case - array of length 1
      ([42], 1, [42]),
      # Reverse sorted array
      ([5, 4, 3, 2, 1], 4, [1, 2, 3, 4]),
      # Already sorted array
      ([1, 2, 3, 4, 5], 3, [1, 2, 3]),
      # Edge case - empty array
      ([], 0, []),
      # Array with negative numbers
      ([-3, -1, -4, -2], 3, [-4, -3, -2]),
      # Mix of positive and negative
      ([-5, 3, -2, 8, -1], 4, [-5, -2, -1, 3]),
      # Large numbers
      ([10**9, -(10**9), 0], 2, [-(10**9), 0])
  ]

#  solutions = [
 #      ('my_solution', solution)
      #('first_k_sorting', first_k_sorting),
      #('first_k_max_heap', first_k_max_heap),
      #('first_k_min_heap', first_k_min_heap),
      #('first_k_quickselect', first_k_quickselect)
  #]

  #for name, solution in solutions:
  for arr, k, want in tests:
      got = solution(arr.copy(), k)
      assert sorted(got) == sorted(want), f"\n({arr}, {k}): got: {got}, want: {want} (in any order)\n"

run_tests()
