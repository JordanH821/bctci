def solution(s: str, brackets: list[str]) -> bool:
    stack: list[str] = []
    # closing to opening bracket map
    bracket_map: dict[str, str] = {bracket[1]: bracket[0] for bracket in brackets}
    # opening brackets 
    open_brackets: set[str] = list(bracket_map.values())
    for char in s:
        if char in open_brackets:
            # add opening brackets to stack
            stack.append(char)
        elif char in bracket_map:
            # closing bracket
            if not stack or stack[-1] != bracket_map[char]:
                # empty stack or opening does not match top of stack
                return False
            else:
                # top of stack matches so pop
                stack.pop()
        else:
            # non-bracket char
            continue
    return not stack

#RUNTIME: O(n), we have to touch every char
#  SPACE: O(b) where b is the number of brackets

def run_tests():
  tests = [
      # Example 1 from book
      ("((a+b)*[c-d]-{e/f})", ["()", "[]", "{}"], True),
      # Example 2 from book
      ("()[}", ["()", "[]", "{}"], False),
      # Example 3 from book
      ("([)]", ["()", "[]", "{}"], False),
      # Example 4 from book
      ("<div> hello :) </div>", ["<>", "()"], False),
      # Example 5 from book
      (")))(()((", [")("], True),
      # Empty string
      ("", ["()"], True),
      # Single character
      ("(", ["()"], False),
      # Multiple bracket types
      ("<<>>()[]{}", ["<>", "()", "[]", "{}"], True),
      # Nested brackets
      ("[{()}]", ["()", "[]", "{}"], True),
      # Unmatched opening bracket
      ("(()", ["()"], False),
      # Unmatched closing bracket
      ("())", ["()"], False),
      # Wrong order of closing
      ("({)}", ["()", "{}"], False),
      # Non-bracket characters mixed in
      ("a(b)c[d]e", ["()", "[]"], True),
      # Multiple identical bracket pairs
      ("<<>>", ["<>"], True),
  ]
  for s, brackets, want in tests:
    got = solution(s, brackets)
    assert got == want, f"\ncustom_brackets({s}, {brackets}): got: {got}, want: {want}\n"
    print("PASS")

run_tests()
