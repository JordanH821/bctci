def solution(array: list[str], join_str: str) -> str:
	if not array:
		return ""
	elif len(array) == 1:
		return array[0]
	
	result: list[str] = []
	# loop over all but the last element
	last_element_index: int = len(array)-1
	for index, value in enumerate(array):
		result.append(array[index])
		if index != last_element_index:
			result.append(join_str)
	return "".join(result)

# RUNTIME: O(n) where n is the number of characters in the final result string: len of array strings + (len(array)-1) * len(join_str)
# SPACE: O(n) since we create the result string

def run_tests():
  tests = [
      # Example 1 from the book
      (["join", "by", "space"], " ", "join by space"),
      # Example 2 from the book
      (["b", "", "k", "", "p", "r n", "", "d", "d!!"],
          "ee", "beeeekeeeepeer neeeedeed!!"),
      # Edge case - empty arrays
      ([], "x", ""),
      ([], "", ""),
      ([], "long separator", ""),
      # Edge case - single element arrays
      (["a"], "x", "a"),
      ([""], "x", ""),
      (["multiple words"], "x", "multiple words"),
      # two element arrays
      (["a", "b"], "", "ab"),
      (["a", "b"], " ", "a b"),
      (["", ""], ",", ","),
      # Edge case - empty strings in array
      (["", "", ""], ",", ",,"),
      (["hello", "", "world"], " ", "hello  world"),
      # special characters
      (["\n", "\t"], ",", "\n,\t"),
      (["tab", "separated"], "\t", "tab\tseparated"),
      # long separators
      (["short", "strings"], "very long separator",
       "shortvery long separatorstrings"),
      # mixed content
      (["123", "abc", "!@#", "   "], "|", "123|abc|!@#|   "),
      # whitespace handling
      (["  leading", "trailing  ", "  both  "],
          "|", "  leading|trailing  |  both  "),
      # numbers and special chars
      (["123", "456"], "-", "123-456"),
      (["!@#", "$%^"], "&", "!@#&$%^"),
  ]
  for arr, s, want in tests:
    got = solution(arr, s)
    assert got == want, f"\njoin({arr}, {s}): got: {got}, want: {want}\n"
    print("PASS")

run_tests()
