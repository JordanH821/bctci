def is_contained(smaller, larger):
    (sx, sy), sr = smaller
    (lx, ly), lr = larger
    # top
    return all(
        [
            (sx + sr) < (lx + lr),  # RIGHT
            (sx - sr) > (lx - lr),  # LEFT
            (sy + sr) < (ly + lr),  # TOP
            (sy - sr) > (ly - lr),  # BOTTOM
        ]
    )


def solution(circles) -> bool:
    if len(circles) == 1:
        return True
    circles.sort(key=lambda circle: circle[1], reverse=True)
    for index in range(len(circles) - 1):
        if not is_contained(circles[index + 1], circles[index]):
            return False
    return True


# RUNTIME: O(n log n) for the circle sorting
# SPACE: O(n) no extra space, but used sort() which takes linear space

def run_tests():
  tests = [
    # Example 1 from the book
    ([((4, 4), 5), ((8, 4), 2)], False),
    # Example 2 from the book
    ([((5, 3), 3), ((5, 3), 2), ((4, 4), 5)], True),
    # Example 3 from the book
    ([((5, 3), 3)], True),
    # Edge case - two identical circles
    ([((1, 1), 2), ((1, 1), 2)], False),
    # Edge case - touching circles
    ([((0, 0), 4), ((0, 0), 2)], True),
    # Edge case - empty list
    ([], True),
    # Edge case - negative coordinates
    ([((-5, -3), 4), ((-5, -3), 2)], True),
    # Edge case - negative radius
    ([((0, 0), -2)], True),
    # Edge case - max coordinate values
    ([((10000, 10000), 10000), ((0, 0), 100)], False),
    # Edge case - min coordinate values
    ([((-10000, -10000), 10000), ((0, 0), 100)], False),
    # Edge case - multiple circles with same center
    ([((1, 1), 5), ((1, 1), 4), ((1, 1), 3), ((1, 1), 2)], True),
    # Edge case - circles not sorted by radius
    ([((0, 0), 2), ((0, 0), 4), ((0, 0), 3)], True),
  ]
  for circles, want in tests:
    got = solution(circles)
    assert got == want, f"\nare_circles_nested({circles}): got: {got}, want: {want}\n"
    print("PASS")

run_tests()