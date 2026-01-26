def solution(array: list[int], low: int, high: int) -> list[int]:
	i: int = 0
	value: int = low
	result: int = []
	while i < len(array) and value <= high:
		if array[i] > value:
			result.append(value)
			value += 1
		elif array[i] == value:
			value +=1 
			i += 1
		else:
			i += 1

	while value <= high:
		result.append(value)
		value += 1

	return result

#RUNTIME: O(n + m), n is the lenght of array and m is the length of the range low to high
#SPACE: O(m), because of the result array

def run_tests():
  tests = [
      # Example 1 from the book
      ([6, 9, 12, 15, 18], 9, 13, [10, 11, 13]),
      # Example 2 from the book
      ([], 9, 9, [9]),
      # Example 3 from the book
      ([6, 7, 8, 9], 7, 8, []),
      # Additional test cases
      ([], 1, 5, [1, 2, 3, 4, 5]),
      ([1, 2, 3, 4, 5], 1, 5, []),
      ([1, 3, 5], 1, 5, [2, 4]),
      ([1], 1, 1, []),
      ([2], 1, 3, [1, 3]),
  ]
  for arr, low, high, want in tests:
    got = solution(arr, low, high)
    assert got == want, f"\nmissing_numbers({arr}, {low}, {high}): got: {got}, want: {want}\n"
    print("PASS")

run_tests()
