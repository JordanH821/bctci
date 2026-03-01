def solution(s: str) -> int:
    count: int = 0
    splits: int = 0
    for char in s:
        if char == "(":
            count += 1
        else:
            count -= 1

        if count == 0:
            splits += 1
    return splits

# RUNTIME: O(n), we have to check every character
#   SPACE: O(1), no extra space

def run_tests():
  tests = [
      ("((()))(()())()(()(()))", 4),
      ("()()()", 3),
      ("(((())))", 1),
      ("", 0),
      ("()", 1),
  ]
  for s, want in tests:
    got = solution(s)
    assert got == want, f"\nmax_balanced_partition({s}): got: {got}, want: {want}\n"
    print("PASS")

run_tests()
