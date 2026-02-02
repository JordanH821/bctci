from typing import Optional

def solution(conns) -> str:
    if not conns:
         return None
    users_to_conns: dict[str, int] = {}
    for _, user in conns:
        if user in users_to_conns:
            users_to_conns[user] += 1
        else:
            users_to_conns[user] = 1
    
    max_conn: int = 0
    max_user: Optional[str] = None
    for user, conn_count in users_to_conns.items():
        if max_conn < conn_count:
            max_conn = conn_count
            max_user = user
    return max_user
     
def run_tests():
  tests = [
      # Example 
      ([("203.0.113.10", "mike"), ("208.51.100.25", "bob"),
        ("202.0.2.5", "mike"), ("203.0.113.15", "bob2")], "mike"),
      # Additional test cases
      ([], None),
      ([("1.1.1.1", "alice")], "alice"),
      ([("1.1.1.1", "alice"), ("1.1.1.2", "bob"),
        ("1.1.1.3", "alice"), ("1.1.1.4", "bob")], "alice"),
  ]
  for connections, want in tests:
    got = solution(connections)
    assert got == want or (want and got and
                           len([(ip, u) for ip, u in connections if u == got]) ==
                           len([(ip, u) for ip, u in connections if u == want])), \
        f"\nmost_shared_account({connections}): got: {got}, want: {want}\n"
    print("PASS")

run_tests()