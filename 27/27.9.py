def solution(array:list[int]) -> list[int]:
	if not array:
		return array

	min_index: int = 0
	min_value: int = array[0]
	for index, value in enumerate(array):
		if value < min_value:
			min_value = value
			min_index = index

	l: int = min_index -1
	r: int = min_index

	result: list[int] = []
	while l >= 0 and r < len(array):
		if array[l] < array[r]:
			result.append(array[l])
			l -= 1
		else:
			result.append(array[r])
			r += 1

	while l >= 0:
		result.append(array[l])
		l -= 1
	
	while r < len(array):
		result.append(array[r])
		r += 1
	
	return result

#RUNTIME: O(n), where n is the lenght of the array
#SPACE: O(n), for the result array

def run_tests():
  tests = [
      # Example 1 from the book
      ([8, 4, 2, 6], [2, 4, 6, 8]),
      # Example 2 from the book
      ([1, 2], [1, 2]),
      # Example 3 from the book
      ([2, 2, 1, 1], [1, 1, 2, 2]),
      # Additional test cases
      ([], []),
      ([1], [1]),
      ([3, 2, 1, 4], [1, 2, 3, 4]),
      ([5, 4, 3, 2, 1, 2, 3], [1, 2, 2, 3, 3, 4, 5]),
      ([1, 1, 1, 1], [1, 1, 1, 1]),
  ]
  for arr, want in tests:
    got = solution(arr)
    assert got == want, f"\nsort_valley_array({arr}): got: {got}, want: {want}\n"
    print("PASSED")

run_tests()
