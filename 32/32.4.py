def solution(actions) -> str:
    stack: list[str] = []
    for action in actions:
        if action[0] == "go":
            stack.append(action[1])
        else:
            for _ in range(action[1]):
                if len(stack) <= 1:
                    break
                else:
                    stack.pop()
    return stack[-1]


# RUNTIME: O(n) where n is the number of actions, the nested loop with only ever traverse up to n back
# SPACE: O(n) in the case where the actions are all "go"


def run_tests():
    tests = [
        (
            [
                ["go", "google.com"],
                ["go", "wikipedia.com"],
                ["go", "amazon.com"],
                ["back", 4],
                ["go", "youtube.com"],
                ["go", "netflix.com"],
                ["back", 1],
            ],
            "youtube.com",
        ),
        ([["go", "example.com"], ["back", 1]], "example.com"),
        (
            [["go", "site1.com"], ["go", "site2.com"], ["back", 1], ["back", 1]],
            "site1.com",
        ),
    ]
    for actions, want in tests:
        got = solution(actions)
        assert got == want, f"\ncurrent_url({actions}): got: {got}, want: {want}\n"
        print("PASS")


run_tests()
