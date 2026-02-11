def get_octet(ip) -> str:
    octet: list[str] = []
    for char in ip:
        if char == ".":
            break
        else:
            octet.append(char)
    return "".join(octet)

def solution(ips: list[str]) -> str:
    octets: dict[str, int] = {}
    for ip in ips:
        octet: str = get_octet(ip)
        if octet not in octets:
            octets[octet] = 0
        octets[octet] += 1

    max_count: int = 0
    max_oct: str = None
    for octet, count in octets.items():
        if count > max_count:
            max_oct = octet
            max_count = count
    return max_oct

# Runtime: O(n) where n is the number of ips, get_octet is O(1) since it will only ever run 4 times and will only ever accumulate three characters
# Space: O(1) since the map will have at most 256 values

def run_tests():
  tests = [
      # Example
      (["203.0.113.10", "208.51.100.5", "202.0.2.5", "203.0.113.5"], "203"),
      # Additional test cases
      ([], None),
      (["192.168.1.1"], "192"),
      (["10.0.0.1", "10.0.0.2", "192.168.1.1"], "10"),
      (["172.16.0.1", "172.16.0.2", "172.17.0.1", "172.16.0.3"], "172"),
  ]
  for ips, want in tests:
    got = solution(ips)
    assert got == want, f"\nmost_frequent_octet({ips}): got: {got}, want: {want}\n"
    print("PASS")

run_tests()
