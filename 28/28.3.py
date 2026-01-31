def is_valid(r, c, n) -> bool:
        return 0 <= r <  n and 0 <= c < n

def can_change_direction(board, r, c):
        return is_valid(r, c, len(board)) and board[r][c] == None

def solution(n: int) -> list[list[int]]:
    board: list[list[int]] = [[None]*n for _ in range(n)]
    directions = [[1,0], [0,-1], [-1,0], [0,1]]
    r: int = n // 2
    c: int = n // 2
    direction_index: int = len(directions)-1
    for num in range(n**2):
        board[r][c] = num
        curr_direction = directions[direction_index % len(directions)]
        next_direction = directions[(direction_index + 1) % len(directions)]
        next_r: int = r + next_direction[0]
        next_c: int = c + next_direction[1]
        if can_change_direction(board, next_r, next_c):
            # If we can change direction we should
            r = next_r
            c = next_c
            direction_index += 1
        else:
            # Stay in current direction
            r += curr_direction[0]
            c += curr_direction[1]
    return board

#RUNTIME: O(n^2)
#SPACE: O(n^2)

def run_tests():
  tests = [
      # Example from book
      (5, [
          [16, 17, 18, 19, 20],
          [15, 4, 5, 6, 21],
          [14, 3, 0, 7, 22],
          [13, 2, 1, 8, 23],
          [12, 11, 10, 9, 24]
      ]),
      # Edge case - 1x1
      (1, [[0]]),
      # Edge case - 3x3
      (3, [
          [4, 5, 6],
          [3, 0, 7],
          [2, 1, 8]
      ]),
  ]

  for n, want in tests:
    got = solution(n)
    assert got == want, f"\nspiral({n}): got: {got}, want: {want}\n"
    print("PASS")

run_tests()