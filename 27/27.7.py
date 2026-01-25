def solution(array: list[int]) -> bool:
	l: int = 0
	r: int = len(array)-1
	while l < r and array[l] <= 0 and array[r] >= 0:
		if array[l] + array[r] == 0:
			return True
		elif abs(array[l]) < abs(array[r]):
			r -= 1
		else:
			l += 1
	return False

RUNTIME: O(n), where n is the length of array
SPACE: O(1), no extra space used

def run_tests():
  tests = [
      # Example 1 from the book
      ([-5, -2, -1, 1, 1, 10], True),
      # Example 2 from the book
      ([-3, 0, 0, 1, 2], True),
      # Example 3 from the book
      ([-5, -3, -1, 0, 2, 4, 6], False),
      # Additional test cases
      ([], False),
      ([0], False),
      ([-1, 1], True),
      ([-2, -1, 0, 1], True),
      ([1, 2, 3, 4], False),
  ]
  for arr, want in tests:
    got = solution(arr)
    assert got == want, f"\ntwo_sum({arr}): got: {got}, want: {want}\n"
    print("PASS")

run_tests()
