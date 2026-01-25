import math

def is_before(pages: list[int], per_day: int, max_days: int) -> bool:
    days: int = 0
    for page_count in pages:
        days += math.ceil(page_count / per_day)
    return days > max_days

def solution(pages: list[int], days: int) -> int:
    l: int = 1
    r: int = max(pages)
    # Assumption with l=1 is that 1 page a day will not finish, so we need to check days > r here since that will be less than 1 page a day
    if not is_before(pages, 1, days):
        return 1
    while r-l>1:
        mid: int = (l+r)//2
        if is_before(pages, mid, days):
            l = mid
        else:
            r = mid
    return r

def run_tests():
  tests = [
      # Example from book
      ([20, 15, 17, 10], 5, 17),

      ([20, 15, 17, 10], 14, 5),
      ([20, 15, 17, 10], 17, 4),
      # Edge case - single chapter
      ([10], 5, 2),
      # Edge case - days = chapters
      ([1, 2, 3], 3, 3),
      # Edge case - more days than max chapter pages
      ([20], 21, 1),
      ([20, 20], 21, 2)
  ]

  for page_counts, days, want in tests:
    got = solution(page_counts, days)
    assert got == want, f"\nmin_pages_per_day({page_counts}, {days}): got: {got}, want: {want}\n"
    print("PASS")

run_tests()

