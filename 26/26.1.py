def solution(s: str, split_char: str) -> list[str]:
	if not s:
		return []
	result: list[str] = []
	curr: list[str] = []
	for s_char in s:
		if s_char == split_char:
			result.append("".join(curr))
			curr = []
		else:
			curr.append(s_char)
	result.append("".join(curr))	
	return result

print(solution("split by space", " "))
print(solution("beekeeper needed", "e"))
print(solution("", "?"))
print(solution("/home/./..//Documents/", "/"))

def run_tests():
  tests = [
      # Example 1 from the book
      ("split by space", ' ', ["split", "by", "space"]),
      # Example 2 from the book
      ("beekeeper needed", 'e', ["b", "", "k", "", "p", "r n", "", "d", "d"]),
      # Example 3 from the book
      ("/home/./..//Documents/", '/',
          ["", "home", ".", "..", "", "Documents", ""]),
      # Example 4 from the book
      ("", '?', []),
      # Edge case - empty string with various delimiters
      ("", ' ', []),
      ("", '\n', []),
      ("", '', []),
      # Edge case - single character string
      ("a", 'a', ["", ""]),
      ("a", 'b', ["a"]),
      # Edge case - no splits
      ("hello", 'x', ["hello"]),
      ("hello", '?', ["hello"]),
      # Edge case - all splits
      ("aaa", 'a', ["", "", "", ""]),
      # Edge case - special characters
      ("\n\n\n", '\n', ["", "", "", ""]),
      ("tab\tseparated\ttext", '\t', ["tab", "separated", "text"]),
      # Edge case - consecutive delimiters
      ("one,,two,,,three", ',', ["one", "", "two", "", "", "three"]),
      # Edge case - delimiter at start/end
      (",start,middle,end,", ',', ["", "start", "middle", "end", ""]),
      # Edge case - mixed length strings
      ("short,medium string,very very long string", ',', [
          "short", "medium string", "very very long string"]),
      # Edge case - whitespace handling
      ("  leading space", ' ', ["", "", "leading", "space"]),
      ("trailing space  ", ' ', ["trailing", "space", "", ""]),
      # Edge case - numbers and special chars
      ("123,456,789", ',', ["123", "456", "789"]),
      ("!@#$%", '@', ["!", "#$%"]),
  ]
  for s, c, want in tests:
    got = solution(s, c)
    assert got == want, f"\nsplit({s}, {c}): got: {got}, want: {want}\n"
    print("PASS")

run_tests()

# RUNTIME: O(n) where n is the number of characters in s
# SPACE: O(n)
