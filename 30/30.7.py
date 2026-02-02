class Checker:
    @classmethod
    def _get_index(cls, c: str) -> int:
        return ord(c) - ord("a")

    @classmethod
    def _make_map(cls, s: str) -> list[int]:
        chars: list[int] = [0] * 26
        for char in s:
            chars[Checker._get_index(char)] += 1
        return chars

    def __init__(self, s: str):
        self._s: str = s
        self._map: list[int] = Checker._make_map(self._s)

    def expands_into(self, s2: str) -> bool:
        if len(s2) - 1 != len(self._s):
            return False
        map: list[int] = Checker._make_map(s2)
        diff_seen: bool = False
        for s_char_count, s2_char_count in zip(self._map, map):
            curr_diff = s_char_count != s2_char_count
            if diff_seen and curr_diff:
                return False
            diff_seen |= curr_diff
        return True


def run_tests():
    tests = [
        # Example 1
        (
            (
                "tea",
                [
                    ("tea", False),
                    ("team", True),
                    ("seam", False),
                ],
            )
        ),
        # Example 2
        (
            (
                "on",
                [
                    ("nooo", False),
                    ("not", True),
                    ("now", True),
                ],
            )
        ),
        # Additional test cases
        (
            (
                "",
                [
                    ("a", True),
                    ("", False),
                    ("ab", False),
                ],
            )
        ),
        (
            (
                "xyz",
                [
                    ("wxyz", True),
                    ("xyzw", True),
                    ("xyza", True),
                    ("xyz", False),
                ],
            )
        ),
    ]

    for s, checks in tests:
        checker = Checker(s)
        for s2, want in checks:
            got = checker.expands_into(s2)
            assert (
                got == want
            ), f"\nChecker({repr(s)}).expands_into({repr(s2)}): got: {got}, want: {want}\n"
            print("PASS")


run_tests()
