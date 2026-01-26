def solution(array: list[str]) -> list[str]:
	R: str = 'R'
	B: str = 'B'
	W: str = 'W'
	
	l: int = 0
	r: int = len(array)-1
	# put all R before W *AND* B
	while l < r:
		if array[l] == R:
			l += 1 
		elif array[r] != R:
			r -= 1
		else:
			tmp = array[l]
			array[l] = R
			array[r] = tmp
			l += 1
			r -= 1
	
	l: int = 0
	r: int = len(array)-1
	# put all W before B
	while l < r:
		if array[l] != B:
			l += 1
		elif array[r] != W:
			r -= 1
		else:
			array[l] = W
			array[r] = B
			l += 1
			r -= 1

	return array

def solution2(array: list[str]) -> list[str]:
	r_count: int = 0
	w_count: int = 0
	for c in array:
		if c == 'R':
			r_count += 1
		elif c == 'W':
			w_count += 1
	i: int = 0
	for _ in range(r_count):
		array[i] = 'R'
		i += 1
	for _ in range(w_count):
		array[i] = 'W'
		i += 1
	while i < len(array):
		array[i] = 'B'
		i += 1
	return array
	
		
		


def run_tests():
  tests = [
      # Example from the book
      (list("RWBBWRW"), list("RRWWWBB")),
      # Additional test cases
      ([], []),
      (list("R"), list("R")),
      (list("W"), list("W")),
      (list("B"), list("B")),
      (list("RW"), list("RW")),
      (list("WR"), list("RW")),
      (list("RWB"), list("RWB")),
      (list("RRRWWBBB"), list("RRRWWBBB")),
      (list("BBBWWRRR"), list("RRRWWBBB")),
  ]
  for arr, want in tests:
    arr_copy = arr.copy()  # Make a copy since function modifies in place
    solution2(arr_copy)
    assert arr_copy == want, f"\nsort_colors({arr}): got: {arr_copy}, want: {want}\n"
    print("PASS")

run_tests()			
