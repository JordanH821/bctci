import typing

def solution(a1: list[int], a2: list[int], a3: list[int]) -> list[int]:
	i1: int = 0
	i2: int = 0
	i3: int = 0
	result: list[int] = []
	while i1 < len(a1) or i2 < len(a2) or i3 < len(a3):
		values: list[int] = []
		if i1 < len(a1):
			values.append(a1[i1])
		if i2 < len(a2):
			values.append(a2[i2])
		if i3 < len(a3):
			values.append(a3[i3])

		min_value: int = min(values)
		if i1 < len(a1) and a1[i1] == min_value:
			i1 += 1
		elif i2 < len(a2) and a2[i2] == min_value:
			i2 += 1
		elif i3 < len(a3) and a3[i3] == min_value:
			i3 += 1

		if result and result[-1] == min_value:
			# skip duplicate
			continue
		else:
			result.append(min_value)
	return result

#RUNTIME: O(n1 + n2 + n3), where nX is the respective array length
#SPACE: O(n1 + n2 + n3), because we built the result array

def run_tests():
  tests = [
      # Example from the book
      ([2, 3, 3, 4, 5, 7], [3, 3, 9], [3, 3, 9], [2, 3, 4, 5, 7, 9]),
      # Additional test cases
      ([], [], [], []),
      ([1], [], [], [1]),
      ([1], [1], [1], [1]),
      ([1, 2, 3], [2, 3, 4], [3, 4, 5], [1, 2, 3, 4, 5]),
      ([1, 1, 1], [1, 1], [1], [1]),
      ([1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]),
  ]
  for arr1, arr2, arr3, want in tests:
    got = solution(arr1, arr2, arr3)
    assert got == want, f"\nthree_way_merge({arr1}, {arr2}, {arr3}): got: {got}, want: {want}\n"
    print("PASS")

run_tests()
