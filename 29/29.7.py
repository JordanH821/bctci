def get_index(n: int, width: int) -> int:
	return [n // width, n % width]

def get_value(grid, n: int, width: int) -> int:
	indices = get_index(n, width)
	return grid[indices[0]][indices[1]]

def solution(grid: list[list[int]], target: int) -> list[int]:
	if grid[0][0] == target:
		return [0,0]
	width: int = len(grid[0])
	height: int = len(grid)
	l: int = 0
	r: int = width * height - 1
	while r - l > 1:
		mid =(l+r)//2
		if get_value(grid, mid, width) < target:
			l = mid
		else:
			r = mid
	return get_index(r, width) if  get_value(grid, r, width) == target else [-1,-1]

def run_tests():
  tests = [
      ([[1, 3, 5], [7, 9, 11], [13, 15, 17]], 9, [1, 1]),  # Example 1
      ([[1, 3, 5], [7, 9, 11]], 4, [-1, -1]),  # Example 2
      ([[2, 3], [4, 5]], 1, [-1, -1]),  # 2x2 grid, all grid after
      ([[1, 2], [3, 4]], 5, [-1, -1]),  # 2x2 grid, all grid before
      ([[1, 2], [3, 4], [5, 6]], 1, [0, 0]),  # 3x2 grid, first element
      ([[1, 2, 3], [4, 5, 6]], 6, [1, 2]),  # 2x3 grid, last element
      ([[7]], 7, [0, 0]),  # Single element edge case
      ([[7]], 6, [-1, -1])  # Single element edge case (not found)
  ]

  for grid, target, want in tests:
    got = solution(grid, target)
    assert got == want, (f"\nsearch_in_sorted_grid({grid}, {target}): got: {got}, want: {want}\n")
    print("PASS")
run_tests()
