def solution(arr: list[str]) -> list[str]:
    n: int = len(arr) // 3
    # swap 1 with 3
    for i in range(n):
        swap_index: int = i + 2 * n
        tmp: str = arr[i]
        arr[i] = arr[swap_index]
        arr[swap_index] = tmp
    # swap 1 with 2
    for i in range(n):
        swap_index: int = i + n
        tmp: str = arr[i]
        arr[i] = arr[swap_index]
        arr[swap_index] = tmp
    return arr

def run_tests():
  tests = [
      # Example from the book
      (list("badreview"), list("reviewbad")),
      # Additional test cases
      ([], []),
      (list("abc"), list("bca")),
      (list("abcdef"), list("cdefab")),
      (list("123456789"), list("456789123")),
      (list("aaabbbccc"), list("bbbcccaaa")),
  ]
  for arr, want in tests:
    arr_copy = arr.copy()  # Make a copy since swap_prefix_suffix modifies in place
    solution(arr_copy)
    assert arr_copy == want, f"\nswap_prefix_suffix({arr}): got: {arr_copy}, want: {want}\n"
    print("PASS")

run_tests()
