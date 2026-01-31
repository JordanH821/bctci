def is_next(grid:list[list[int]], r: int, c: int) -> bool:
	return c < len(grid[0]) and 0 <= r < len(grid) and grid[r][c] == 1
	
def solution(grid: list[list[int]]):
    r: int = 0
    for i in range(len(grid)):
        # Find the starting row of the fox
        if grid[i][0] == 1:
            r = i
            break
    min_distance: int = r
    directions: list[int] = [-1, 0, 1]
    for c in range(1, len(grid[0])):
        for r_change in directions:
            new_r: int = r + r_change
            if is_next(grid, new_r, c):
                min_distance = min(min_distance, new_r)
                r = new_r
                break
    return min_distance


def run_tests():
    tests = [
      # Example from book
      ([[0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [1, 1, 0, 1, 0, 0],
        [0, 0, 0, 0, 1, 1]], 1),
      # Edge case - top of grid
      ([[1, 1, 1, 1],
        [0, 0, 0, 0],
        [0, 0, 0, 0]], 0),
      # Edge case - bottom of grid
      ([[0, 0, 0, 0],
        [0, 0, 0, 0],
        [1, 1, 1, 1]], 2),
      # Edge case - single column
      ([[0], [1], [0]], 1),
      # Edge case - single row
      ([[1]], 0),
      # Edge case - zigzag path
      ([[0, 0, 0, 0],
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 1]], 1),
      # Test max up/down movement
      ([[0, 0, 0, 0],
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]], 1),
      # Test staying at same level
      ([[0, 0, 0, 0],
        [1, 1, 1, 1],
        [0, 0, 0, 0]], 1),
      # Test going up then down
      ([[0, 0, 0, 0],
        [1, 0, 0, 0],
        [0, 1, 1, 0],
        [0, 0, 0, 1]], 1)
  ]

    for field, want in tests:
        got = solution(field)
        assert got == want, f"\ndistance_to_river({field}): got: {got}, want: {want}\n"
        print("PASS")

run_tests()
                        
