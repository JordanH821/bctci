def solution(a1: list[list[int]], a2: list[list[int]]) -> list[list[int]]:
    i1: int = 0
    i2: int = 0
    result: list[list[int]] = []
    while i1 < len(a1) and i2 < len(a2):
        if a1[i1][0] > a2[i2][1]:
            # no intersection and a2 is less
            i2 += 1
        elif a1[i1][1] < a2[i2][0]:
            # no intersection and a1 is less
            i1 += 1
        else:
            min_value: int = max(a1[i1][0], a2[i2][0])
            max_value: int = min(a1[i1][1], a2[i2][1])
            result.append([min_value, max_value])
            if a1[i1][1] > a2[i2][1]:
                i2 += 1
            else:
                i1 += 1
    return result

def run_tests():
  tests = [
      # Example 1 from the book
      ([[0, 1], [4, 6], [7, 8]], [[2, 3], [5, 9], [10, 11]], [[5, 6], [7, 8]]),
      # Example 2 from the book
      ([[2, 4], [5, 8]], [[3, 3], [4, 7]], [[3, 3], [4, 4], [5, 7]]),
      # Additional test cases
      ([], [], []),
      ([[1, 2]], [], []),
      ([[1, 3]], [[2, 4]], [[2, 3]]),
      ([[1, 5]], [[2, 3]], [[2, 3]]),
      ([[1, 2], [3, 4]], [[2, 3]], [[2, 2], [3, 3]]),
  ]
  for arr1, arr2, want in tests:
    got = solution(arr1, arr2)
    assert got == want, f"\ninterval_intersection({arr1}, {arr2}): got: {got}, want: {want}\n"
    print("PASS")

run_tests()


