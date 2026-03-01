def solution(s: str) -> str:
    stack: list[str] = []
    result: list[str] = []
    for char in s:
        if char == ")" and stack and stack[-1] == "(":
            result.append("(")
            count -= 1
        elif char == "(":
            result.append("(")
            count += 1
    while count > 0:
        result.pop()
        count -=1
    return "".join(result)

def run_tests():
  tests = [
      ("))(())(()", ["(())()"]),
      ("(()()", ["()()", "(())"]),
      ("(()(()(", ["()()", "(())"]),
      ("())(()", ["()()"]),
      ("(", [""]),
      ("", [""]),
  ]
  for s, want in tests:
    got = solution(s)
    assert got in want, f"\nlongest_balanced_subsequence({s}): got: {got}, want: {want}\n"
    print("PASS")

run_tests()
