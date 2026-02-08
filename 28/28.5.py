def check_rows(board: list[list[int]]) -> bool:
    for row in range(9):
        seen: list[int] = [False] * 10
        for col in range(9):
            value: int = board[row][col]
            if value != 0:
                if seen[value]:
                    return False
                seen[value] = True
    return True


def check_cols(board: list[list[int]]) -> bool:
    for col in range(9):
        seen: list[int] = [False] * 10
        for row in range(9):
            value: int = board[row][col]
            if value != 0:
                if seen[value]:
                    return False
                seen[value] = True
    return True


def check_subgrids(board: list[list[int]]) -> bool:
    for col in range(0, 9, 3):
        for row in range(0, 9, 3):
            seen: list[int] = [False] * 10
            for row_offset in range(3):
                for col_offset in range(3):
                    value: int = board[row + row_offset][col + col_offset]
                    if value != 0:
                        if seen[value]:
                            return False
                        seen[value] = True
    return True


def solution(board: list[list[int]]) -> bool:
    return check_rows(board) and check_cols(board) and check_subgrids(board)

#RUNTIME: O(1) always a 9x9 grid
#SPACE: O(1) only track 0-9 each iteration


def run_tests():
    tests = [
        # Example 1 from book - valid sudoku
        (
            [
                [5, 0, 0, 0, 0, 0, 0, 0, 6],
                [0, 0, 9, 0, 5, 0, 3, 0, 0],
                [0, 3, 0, 0, 0, 2, 0, 0, 0],
                [8, 0, 0, 7, 0, 0, 0, 0, 9],
                [0, 0, 2, 0, 0, 0, 8, 0, 0],
                [4, 0, 0, 0, 0, 6, 0, 0, 3],
                [0, 0, 0, 3, 0, 0, 0, 4, 0],
                [0, 0, 3, 0, 8, 0, 2, 0, 0],
                [9, 0, 0, 0, 0, 0, 0, 0, 7],
            ],
            True,
        ),
        # Example 2 from book - invalid sudoku (duplicate 7 in bottom right subgrid)
        (
            [
                [5, 0, 0, 0, 0, 0, 0, 0, 6],
                [0, 0, 9, 0, 5, 0, 3, 0, 0],
                [0, 3, 0, 0, 0, 2, 0, 0, 0],
                [8, 0, 0, 7, 0, 0, 0, 0, 9],
                [0, 0, 2, 0, 0, 0, 8, 0, 0],
                [4, 0, 0, 0, 0, 6, 0, 0, 3],
                [0, 0, 0, 3, 0, 0, 0, 4, 0],
                [0, 0, 3, 0, 8, 0, 7, 0, 0],
                [9, 0, 0, 0, 0, 0, 0, 0, 7],
            ],
            False,
        ),
        # Edge case - empty board
        ([[0] * 9 for _ in range(9)], True),
        # Edge case - full valid board
        (
            [
                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [4, 5, 6, 7, 8, 9, 1, 2, 3],
                [7, 8, 9, 1, 2, 3, 4, 5, 6],
                [2, 3, 1, 5, 6, 4, 8, 9, 7],
                [5, 6, 4, 8, 9, 7, 2, 3, 1],
                [8, 9, 7, 2, 3, 1, 5, 6, 4],
                [3, 1, 2, 6, 4, 5, 9, 7, 8],
                [6, 4, 5, 9, 7, 8, 3, 1, 2],
                [9, 7, 8, 3, 1, 2, 6, 4, 5],
            ],
            True,
        ),
    ]

    for board, want in tests:
        got = solution(board)
        assert got == want, f"\nsolve({board}): got: {got}, want: {want}\n"
        print("PASS")


run_tests()
