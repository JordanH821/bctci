def solution(s: str, target: str) -> int:
	if not s and target:
		# s is empty and target is not
		return -1
	if not target:
		# t is empty, s may or may not be
		return 0
	if len(s) < len(target):
		return -1
	for s_index, s_char in enumerate(s):
		if s_index + len(target) - 1 > len(s): 
			break
		for t_index, t_char in enumerate(target):
			if t_char != s[s_index + t_index]:
				break
			if t_index == len(target)-1:
				return s_index
	return -1

#RUNTIME: O(s*t) where s and t are the length of the search and target strings respectively
#SPACE: O(1) no extra space used

def run_tests():
  tests = [
      # Basic test cases from book
      ("hello world", "world", 6),
      ("hello world", "hello", 0),
      ("needle in a haystack", "needle", 0),
      ("needle in a haystack", "haystack", 12),
      ("needle in a haystack", "not", -1),
      # Edge case - empty strings
      ("", "", 0),
      ("", "x", -1),
      ("x", "", 0),
      ("abc", "", 0),
      # Edge case - single character
      ("x", "x", 0),
      ("abc", "a", 0),
      ("abc", "b", 1),
      ("abc", "c", 2),
      ("abc", "d", -1),
      # Edge case - pattern longer than string
      ("x", "xx", -1),
      ("abc", "abcd", -1),
      # multiple occurrences
      ("banana", "ana", 1),  # Should return first occurrence
      ("banana", "an", 1),   # Should return first occurrence
      ("banana", "a", 1),    # Should return first occurrence
      # overlapping patterns
      ("aaaaa", "aa", 0),
      ("aaaaa", "aaa", 0),
      ("aabaabaa", "aaba", 0),
      # pattern at start/end
      ("startend", "start", 0),
      ("startend", "end", 5),
      # special characters
      ("\n\n\n", "\n", 0),
      ("\n\n\n", "\n\n", 0),
      ("tab\tseparated", "\t", 3),
      # repeated characters
      ("mississippi", "issi", 1),
      ("mississippi", "ssi", 2),
      ("mississippi", "sip", 6),
      # case sensitivity
      ("Hello World", "hello", -1),
      ("Hello World", "Hello", 0),
      # whitespace
      ("   spaces   ", " ", 0),
      ("   spaces   ", "   ", 0),
      ("   spaces   ", "spaces", 3),
      # numbers and special chars
      ("123123", "123", 0),
      ("!@#$%", "@#", 1),
      # long strings and patterns
      ("very very very long string to search in", "very long string", 10),
      ("aaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaa", 0),  # Many matches
  ]
  for s, t, want in tests:
    got = solution(s, t)
    assert got == want, f"\nsolution({s}, {t}): got: {got}, want: {want}\n"
    print("PASS")

run_tests()
