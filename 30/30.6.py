from math import sqrt

def solution(arr: list[list[int]]) -> list[list[int]]:
    map: dict[int, int] = {} # index to value
    result: list[list[int]] = []
    for index, value in enumerate(arr):
        map[value] = index

    for index, value in enumerate(arr):
        squared = value * value
        if squared in map:
            result.append([index, map[squared]])
    return result


def run_tests():
  tests = [
      # Example 
      ([4, 10, 3, 100, 5, 2, 10000], [[5, 0], [1, 3], [3, 6]]),
      # Additional test cases
      ([], []),
      ([1], [[0, 0]]),
      ([2, 4], [[0, 1]]),
  ]
  for arr, want in tests:
    got = solution(arr)
    # Sort both lists to compare them regardless of order
    got.sort()
    want.sort()
    assert got == want, f"\nfind_squared({arr}): got: {got}, want: {want}\n"
    print("PASS")

run_tests()