def solution(a: int, p: int, m: int) -> int:
    if p == 0:
        return 1
    elif p % 2 == 0:
       p2 = solution(a, p//2, m)
       return (p2*p2) %m
    else:
        return (a*solution(a,p-1,m))%m

def run_tests():
  tests = [
    # Example 1 from book
    ((2, 5, 100), 32),
    # Example 2 from book
    ((2, 5, 30), 2),
    # Edge cases
    ((2, 0, 10), 1),
    ((3, 1, 5), 3),
    ((5, 3, 7), 6),
    # Large test case
    ((123456789, 987654321, 1000000007), 652541198),
  ]
  
  for (a, p, m), want in tests:
    got = solution(a, p, m)
    assert got == want, f"\npower({a}, {p}, {m}): got: {got}, want: {want}\n"
    print("PASS")

run_tests()

