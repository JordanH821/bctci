def solution(arr:list[int]) -> int:
    if len(arr) == 1:
        return arr[0]
    if len(arr) == 2:
        return max(max(arr), sum(arr))
    def helper(l, r):
        if r-l == 1:
            return arr[l], arr[l]
        else:
            mid = (l+r)//2
            l_max, l_sum = helper(l, mid)
            r_max, r_sum = helper(mid, r)
            t_sum = l_sum + r_sum
            return max(l_max, r_max, l_sum + r_sum), t_sum
    return max(helper(0, len(arr)))

def run_tests():
  tests = [
      # Example 1 from book
      ([3, -9, 2, 4, -1, 5, 5, -4], 6),
      # Example 2 from book
      ([1], 1),
      # Example 3 from book
      ([-1, -2], -1),
      # Additional test case
      ([1, 2, 3, 4], 10),
      # Additional test case with all negatives
      ([-2, -1, -4, -3], -1),
      # Large test case
      ([1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -
        12, 13, -14, 15, -16], 15),
  ]
  for arr, want in tests:
    got = solution(arr)
    assert got == want, f"\nmax_laminal_sum({arr}): got: {got}, want: {want}\n"
    print("PASS")

run_tests()