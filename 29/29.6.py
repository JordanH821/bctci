def solution(p1: list[int], p2: list[int]) -> int:
	if len(p1) == 2:
		return 1
	l: int = 0
	r: int = len(p1)-1
	while r - l > 1:
		mid: int = (l+r)//2
		if p1[mid] > p2[mid]:
			l = mid
		else:
			r = mid
	return r

#RUNTIME: O(logn) where n is the length of p1 and p2
#SPACE: O(1) 

def run_tests():
  tests = [
      # Example 1 from book
      ([2, 4, 6, 8, 10], [1, 3, 5, 9, 11], 3),
      # Example
      ([2, 3, 4, 5, 6], [1, 2, 3, 6, 7], 3),
      # Example
      ([3, 4, 5], [2, 5, 6], 1),
      # Edge case - overtake at start
      ([2, 3], [1, 4], 1),
  ]

  for p1, p2, want in tests:
    got = solution(p1, p2)
    assert got == want, f"\nrace_overtaking({p1}, {p2}): got: {got}, want: {want}\n"
    print("PASS")

run_tests()
