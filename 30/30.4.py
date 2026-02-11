def solution(users) -> bool:
    ips_set: set[list[str]] = set()
    for user, ips in users:
        ips.sort()
        ip_tup = tuple(ips)
        if ip_tup in ips_set:
            return True
        ips_set.add(ip_tup)
    return False

#RUNTIME: O(n) where n is the number of users, we sort and create tuples of the IPs but they are capped at 10 so they reduce to O(1)
#  SPACE: O(n) we need to store n tuples in the worst case

def run_tests():
  tests = [
      # Example
      ([("mike", ["203.0.3.10", "208.51.0.5", "52.0.2.5"]),
        ("bob", ["111.0.0.10", "222.0.0.5", "222.0.0.8"]),
          ("bob2", ["222.0.0.5", "222.0.0.8", "111.0.0.10"])], True),
      # Additional test cases
      ([], False),
      ([("alice", ["1.1.1.1"])], False),
      ([("alice", ["1.1.1.1", "2.2.2.2"]),
        ("bob", ["2.2.2.2", "1.1.1.1"])], True),
      ([("alice", ["1.1.1.1"]), ("bob", ["2.2.2.2"])], False),
  ]
  for users, want in tests:
    got = solution(users)
    assert got == want, f"\nmulti_account_cheating({users}): got: {got}, want: {want}\n"
    print("PASS")

run_tests()
