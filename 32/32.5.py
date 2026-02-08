def solution(actions) -> str:
    bwd_stack: list[str] = []
    fwd_stack: list[str] = []
    for action in actions:
        if action[0] == "go":
            bwd_stack.append(action[1])
            fwd_stack = []
        elif action[0] == "back":
            for _ in range(action[1]):
                if len(bwd_stack) <= 1:
                    break
                else:
                    fwd_stack.append(bwd_stack.pop())
        else:
            # Forward
            for _ in range(action[1]):
                if not fwd_stack:
                    break
                else:
                    bwd_stack.append(fwd_stack.pop())
    return bwd_stack[-1]
# RUNTIME: O(min(g^2), n)) when g is the total number of go commands and n is the number of actions, we can front load a large number of "go" actions are traverse bwd and fwd over essentially n
# SPACE: O(g) where g is the number of go commands

def solution_efficient(actions) -> str:
    current_site: int = -1
    fwd_available: int = 0
    sites: list[str] = []
    for action in actions:
        if action[0] == "go":
            current_site += 1
            if current_site >= len(sites):
                    sites.append(action[1])
            else:
                sites[current_site] = action[1]
            fwd_available = 0
        elif action[0] == "back":
            current_site = max(current_site-action[1], 0)
        else:
            current_site += min(fwd_available, action[1])

    return sites[current_site]
# RUNTIME: O(n) when n is the number of actions
# SPACE: O(g) where g is the number of go commands


# above keeps all go "sites" uneccesarily, this deletes them when they are not needed anymore
def solution_efficient_with_list_del(actions) -> str:
    current_site: int = -1
    sites: list[str] = []
    for action in actions:
        if action[0] == "go":
            if current_site != len(sites)-1:
                # if we are not at the end remove the fwd section
                # NOTE: this syntax does not create a duplicate array with the slicing, it is overloaded
                del sites[current_site+1:]
            sites.append(action[1])
            current_site += 1
        elif action[0] == "back":
            current_site = max(current_site-action[1], 0)
        else:
            current_site = min(len(sites)-1, current_site + action[1])

    return sites[current_site]
# RUNTIME: O(n) when n is the number of actions
# SPACE: O(g) where g is the number of go commands

def run_tests():
  tests = [
      ([["go", "google.com"], ["go", "wikipedia.com"], ["back", 1], ["forward", 1], [
       "back", 3], ["go", "netflix.com"], ["forward", 3]], "netflix.com"),
      ([["go", "example.com"], ["forward", 1]], "example.com"),
      ([["go", "site1.com"], ["go", "site2.com"], [
       "back", 1], ["forward", 1], ["back", 1]], "site1.com"),
  ]
  for actions, want in tests:
    got = solution(actions)
    assert got == want, f"\ncurrent_url_with_forward({actions}): got: {got}, want: {want}\n"
    print("PASS")
    got = solution_efficient(actions)
    assert got == want, f"\ncurrent_url_with_forward_efficient({actions}): got: {got}, want: {want}\n"
    print("PASS EFF")
    got = solution_efficient_with_list_del(actions)
    assert got == want, f"\ncurrent_url_with_forward_efficient({actions}): got: {got}, want: {want}\n"
    print("PASS EFF W DEL")

run_tests()