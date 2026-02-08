def solution(arr: list[int], k: int) -> list[int]:
    stack: list[tuple[int, int]] = []
    for num in arr:
        if not stack or stack[-1][0] != num:
            # stack is empty or nums are not matching
            stack.append((num, 1))
        else:
            while stack and stack[-1][0] == num and stack[-1][1] == k - 1:
                # while we can compress do it
                stack.pop()
                num = num * k
            # append the possibly compressed value
            if stack and stack[-1][0] == num:
                _, count = stack.pop()
                stack.append((num, count + 1))
            else:
                stack.append((num, 1))
    result: list[int] = []
    for num, count in stack:
        for _ in range(count):
            result.append(num)
    return result

#RUNTIME: O(n), same reasoning as 32.1
#SPACE: O(n), same same
def run_tests():
    tests = [
        ([1, 9, 9, 3, 3, 3, 4], 3, [1, 27, 4]),
        ([8, 4, 2, 2], 2, [16]),
        ([4, 4, 4, 4], 5, [4, 4, 4, 4]),
        ([], 2, []),
        ([0, 0, 0, 0], 2, [0]),
    ]
    for arr, k, want in tests:
        got = solution(arr, k)
        assert (
            got == want
        ), f"\ncompress_array_k({arr}, {k}): got: {got}, want: {want}\n"
        print("PASS")


run_tests()
