def binary_search(array: list[int], target: int, is_before) -> int:
	l = 0
	r = len(array)-1
	if target < array[l] or target > array[r]:
		return -1
	while r - l > 1:
		mid: int = (l+r)//2
		if is_before(array[mid], target):
			l = mid
		else:
			r = mid
	if array[l] != target and array[r] != target:
		return -1
	# return first or last occurrence 
	return l if array[l] == target else r
	

def solution(array: list[int], target: int,  multiple: int) -> bool:
	if len(array) == 1 and array[0] != target:
		# target is not in the array once => k * 0 = 0
		return True
	left: int = 0 if array[0] == target else binary_search(array, target, lambda curr, target: curr < target)
	if left == -1:
		# target not in array
		return True
	right: int = len(array)-1 if array[-1] == target else binary_search(array, target, lambda curr, target: curr <= target)
	return (right-left+1) % multiple == 0


print(solution([1,2,2,2,2,2,2,3], 2, 3))
print(solution([1,2,2,2,2,2,2,3], 2, 4))
print(solution([1,2,2,2,2,2,2,3], 4, 3))

def run_tests():
  tests = [
      # Example 1
      ([1, 2, 2, 2, 2, 2, 2, 3], 2, 3, True),
      # Example 2
      ([1, 2, 2, 2, 2, 2, 2, 3], 2, 4, False),
      # Example 3: 0 occurrences, 0 is multiple of any number
      ([1, 2, 2, 2, 2, 2, 2, 3], 4, 3, True),
      # Example 4
      ([1, 1, 2, 2, 2], 1, 3, False),
      # single occurrence, at the start
      ([1, 3, 5, 7, 9, 11, 13, 15, 17, 19], 1, 1, True),
      ([1, 3, 5, 7, 9, 11, 13, 15, 17, 19], 1, 2, False),
      # single occurrence, at the end
      ([1, 3, 5, 7, 9, 11, 13, 15, 17, 19], 19, 1, True),
      ([1, 3, 5, 7, 9, 11, 13, 15, 17, 19], 19, 2, False),
      # single occurrence, in the middle
      ([1, 3, 5, 7, 9, 11, 13, 15, 17, 19], 9, 1, True),
      ([1, 3, 5, 7, 9, 11, 13, 15, 17, 19], 9, 2, False),
      # smaller than any elements
      ([1, 3, 5, 7, 9, 11, 13, 15, 17, 19], 0, 1, True),
      ([1, 3, 5, 7, 9, 11, 13, 15, 17, 19], 0, 2, True),
      # larger than any elements
      ([1, 3, 5, 7, 9, 11, 13, 15, 17, 19], 20, 1, True),
      ([1, 3, 5, 7, 9, 11, 13, 15, 17, 19], 20, 2, True),
      # Edge case - every occurrence is target
      ([5, 5, 5, 5, 5], 5, 5, True),
      ([5, 5, 5, 5, 5], 5, 3, False),
  ]
  for arr, target, k, want in tests:
    got = solution(arr, target, k)
    assert got == want, f"\ntarget_count_divisible_by_k({arr}, {target}, {k}): got: {got}, want: {want}\n"
    print("PASS")

run_tests()

#RUNTIME: O(2 * logn) ==> O(logn)
#SPACE: O(1)
