def is_valid(board:list[list[int]], r: int, c: int) -> bool:
	return 0 <= r < len(board) and 0 <= c < len(board[0])

def king(board: list[list[int]], r: int, c: int) -> list[list[int]]:
	directions: list[list[int]] = [[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1]]
	result: list[list[int]] = []
	for direction in directions:
		new_r: int = r + direction[0]
		new_c: int = c + direction[1]
		if is_valid(board, new_r, new_c) and board[new_r][new_c] == 0:
			result.append([new_r, new_c])
	return result

def knight(board: list[list[int]], r: int, c: int) -> list[list[int]]:
    directions: list[list[int]] = [[-2,1],[-1,2],[1,2],[2,1],[2,-1],[1,-2],[-1,-2],[-2,-1]]
    result: list[list[int]] = []
    for direction in directions:
            new_r: int = r + direction[0]
            new_c: int = c + direction[1]
            if is_valid(board, new_r, new_c) and board[new_r][new_c] == 0:
                    result.append([new_r, new_c])
    return result

def queen(board: list[list[int]], r: int, c: int) -> list[list[int]]:
    directions: list[list[int]] = [[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1]]
    result: list[list[int]] = []
    for direction in directions:
            new_r: int = r + direction[0]
            new_c: int = c + direction[1]
            while is_valid(board, new_r, new_c) and board[new_r][new_c] == 0:
                    result.append([new_r, new_c])
                    new_r += direction[0]
                    new_c += direction[1]
    return result

def solution(board: list[list[int]], piece: str, r: int, c: int) -> list[list[int]]:
	if piece == "king":
		return king(board, r, c)
	elif piece == "knight":
		return knight(board, r, c)
	else:
		return queen(board, r, c)

def run_tests():
  tests = [
      # Example 1 from the book - king moves
      ([[0, 0, 0, 1, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 1, 0, 1, 1, 0],
        [1, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0]], "king", 3, 5,
          [[2, 5], [3, 4], [4, 4], [4, 5]]),
      # Example 2 from the book - knight moves
      ([[0, 0, 0, 1, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 1, 0, 1, 1, 0],
        [1, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0]], "knight", 4, 3,
       [[2, 2], [3, 5], [5, 5]]),
      # Example 3 from the book - queen moves
      ([[0, 0, 0, 1, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 1, 0, 1, 1, 0],
        [1, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0]], "queen", 4, 4,
       [[3, 4], [3, 5], [4, 0], [4, 1], [4, 2], [4, 3], [4, 5],
        [5, 3], [5, 4], [5, 5]]),
      # Edge case - 1x1 board
      ([[0]], "queen", 0, 0, []),
      # Edge case - all occupied except current position
      ([[1, 1], [1, 0]], "knight", 1, 1, []),
  ]

  for board, piece, r, c, want in tests:
    got = solution(board, piece, r, c)
    # Sort both lists for consistent comparison
    got.sort()
    want.sort()
    assert got == want, (f"\nchess_moves({board}, {piece}, {r}, {c}): got: {got}, want: {want}\n")
    print("PASS")

run_tests()