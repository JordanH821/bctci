class Spreadsheet:
    def __init__(self, rows: int, cols: int):
        self._rows: int = 0
        self._cols: int = 0
        self._sheet: list[list[int]] = []
        self.new(rows, cols)

    def new(self, rows: int, cols: int) -> None:
        self._rows = rows
        self._cols = cols
        self._sheet = [[0 for _ in range(self._cols)] for _ in range(self._rows)]

    def get(self, row: int, col: int) -> int:
        return self._sheet[row][col]

    def set(self, row: int, col: int, val: int) -> None:
        self._sheet[row][col] = val

    def sort_columns_by_row(self, row: int) -> None:
        row_indices: list[int] = [i for i in range(self._cols)]
        row_indices.sort(key=lambda i: self._sheet[row][i])
        for row in range(self._rows):
            self._sheet[row] = [self._sheet[row][idx] for idx in row_indices]

    def sort_rows_by_column(self, col: int) -> None:
        self._sheet.sort(key=lambda r: r[col])


def run_tests():
    tests = [
        # Example from the book
        (
            lambda s: [
                s.new(3, 3),
                s.set(0, 0, 5),
                s.set(0, 1, 3),
                s.set(0, 2, 8),
                s.set(1, 0, 6),
                s.set(2, 1, 1),
                s.sort_columns_by_row(0),
                s.sort_rows_by_column(1),
            ],
            [
                [1, 0, 0],
                [3, 5, 8],
                [0, 6, 0],
            ],
        ),
        # Edge case - 1x1 spreadsheet
        (
            lambda s: [s.new(1, 1), s.set(0, 0, 42)],
            [
                [42],
            ],
        ),
        # Edge case - sort empty rows
        (
            lambda s: [s.new(3, 2), s.sort_rows_by_column(0)],
            [
                [0, 0],
                [0, 0],
                [0, 0],
            ],
        ),
    ]

    for operations, want in tests:
        s = Spreadsheet(0, 0)
        operations(s)
        for r in range(len(want)):
            for c in range(len(want[0])):
                got = s.get(r, c)
                expect = want[r][c]
                assert got == expect, f"\nget({r}, {c}): got: {got}, want: {expect}\n"
                print("PASS")


run_tests()
