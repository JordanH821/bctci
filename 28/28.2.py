def is_valid(board: list[list[int]], r: int, c: int) -> bool:
    return 0 <= r < len(board) and 0 <= c < len(board[0])

def mark_queen_moves(board: list[list[int]], r: int, c: int) -> None:
    directions: list[list[int]] = [[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1]]
    for direction in directions:
        new_r: int = r
        new_c: int = c
        while is_valid(board, new_r, new_c):
            board[new_r][new_c] = 1
            new_r += direction[0]
            new_c += direction[1]

def solution(board: list[list[int]]) -> list[list[int]]:
    # new_board: list[list[int]] = [[0]*len(board)]*len(board)
    # above is bad and creates a list of pointers to the same list: [L, L, L, L] rather than unique [L1, L2, L3, L4]
    new_board: list[list[int]] = [[0] *len(board) for _ in range(len(board))]
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] == 1:
                mark_queen_moves(new_board, r, c)
    return new_board


def run_tests():
  tests = [
      ([[0, 0, 0, 1],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [1, 0, 0, 0]],
       [[1, 1, 1, 1],
        [1, 0, 1, 1],
        [1, 1, 0, 1],
        [1, 1, 1, 1]]),
      # Edge case - 1x1 board with queen
      ([[1]], [[1]]),
      # Edge case - 1x1 board without queen
      ([[0]], [[0]]),
      # Edge case - no queens
      ([[0, 0], [0, 0]], [[0, 0], [0, 0]]),
  ]

  for board, want in tests:
    got = solution(board)
    assert got == want, f"\nsafe_cells({board}): got: {got}, want: {want}\n"
    print("PASS")

run_tests()
