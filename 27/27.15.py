def solution(array: list[int], p: int) -> list[int]:
	l: int = 0
	r: int = len(array)-1
	# strictly greater than to the right of pivot
	while l < r:
		if array[l] <= p:
			l += 1
		elif array[r] > p:
			r -= 1
		else:
			tmp: int = array[l]
			array[l] = array[r]
			array[r] = tmp
			l += 1
			r -= 1
	
	l: int = 0
	r: int = len(array)-1
	# strictly less than to the left of pivot
	while l < r:
		if array[l] < p:
			l += 1
		elif array[r] >= p:
			r -= 1
		else:
			tmp: int = array[l]
			array[l] = array[r]
			array[r] = tmp
			l += 1
			r -= 1

	return array

#RUNTIME: O(n) where n is the lenght of the array
#SPACE: O(1) we move in place


def run_tests():
  
  def is_valid_partition(arr, pivot):
    # Find boundaries between sections
    first = 0
    while first < len(arr) and arr[first] < pivot:
      first += 1
    second = first
    while second < len(arr) and arr[second] == pivot:
      second += 1

    # Check that all elements are in their correct sections
    for i in range(first):
      if arr[i] >= pivot:
        return False
    for i in range(first, second):
      if arr[i] != pivot:
        return False
    for i in range(second, len(arr)):
      if arr[i] <= pivot:
        return False
    return True

  tests = [
      # Example 1 from the book
      ([1, 7, 2, 3, 3, 5, 3], 4),
      # Example 2 from the book
      ([1, 7, 2, 3, 3, 5, 3], 3),
      # Additional test cases
      ([], 1),
      ([1], 1),
      ([1, 2], 1),
      ([2, 1], 1),
      ([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5], 4),
  ]
  for arr, pivot in tests:
    arr_copy = arr.copy()  # Make a copy since partition modifies in place
    solution(arr_copy, pivot)
    assert is_valid_partition(arr_copy, pivot), f"\npartition({arr}, {pivot}): got: {arr_copy}\n"
    print("PASS")

run_tests()
