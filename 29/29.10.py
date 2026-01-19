def solution(capacity: int, scoop: int) -> int:
	l: int = 1
	r: int = 1
	# Find max for r
	while r * scoop <= capacity:
		r *= 2
	while r - l > 1:
		mid = (l+r) >> 1
		if mid * scoop <= capacity:
			l = mid
		else:
			r = mid
	return l

def run_tests():
  tests = [
    # Basic cases
    (10, 2, 5),
    (10, 3, 3),
    (10, 4, 2),
    (10, 5, 2),
    # Large numbers
    (1_000_000, 1, 1_000_000),
    # Large numbers with multiple refills
    (1_000_000, 500_000, 2),
    # Random cases
    (18, 5, 3),
    (182_983, 90, 2033),
  ]

  for a, b, expected in tests:
    result = solution(a, b)
    assert result == expected, f"num_refills({a}, {b}): got {result}, want {expected}"
    print("PASS")

run_tests()
