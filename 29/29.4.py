def helper(a: list[int], target: int) -> int:
	l = 0
	r = len(a)-1
	if a[l] > target or a[r] < target:
		return -1
	if a[l] == target:
		return l
	while r - l > 1:
		mid = (l + r) // 2
		if a[mid] <  target:
			l = mid
		else:
			r = mid
	return r if a[r] == target else -1

def solution(sorted_a: list[int], unsorted_a: list[int]) -> list[int]:
	for unsorted_index, unsorted_value in enumerate(unsorted_a):
		if (sorted_index := helper(sorted_a, -1 * unsorted_value)) != -1:
			return [sorted_index, unsorted_index]
	return [-1,-1]

print(solution([-5, -4, -1, 4, 6, 6, 7], [-3, 7, 18, 4, 6])) # [1,3]
print(solution([1,2,3], [1,2,3])) # [-1,-1]
print(solution([-2,0,1,2], [0,2,-2,4])) # [0,1]

def run_tests():
  tests = [
      # Example from book
      ([-5, -4, -1, 4, 6, 6, 7], [-3, 7, 18, 4, 6], [1, 3]),
      # no solution
      ([1, 2, 3], [1, 2, 3], [-1, -1]),
      ([1], [-1], [0, 0]),
      ([1, 2], [-2, -1], [1, 0]),
      ([0, 1, 2, 3], [3, 2, 1, 0], [0, 3]),
  ]

  for sorted_arr, unsorted_arr, want in tests:
    got = solution(sorted_arr, unsorted_arr)
    assert got == want, f"\ntwo_array_two_sum({sorted_arr}, {unsorted_arr}): got: {got}, want: {want}\n"
    print("PASS")

run_tests()
