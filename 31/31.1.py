from operator import itemgetter

def solution(word: str) -> list[str]:
    map: dict[str, int] = {}
    for char in word:
        if char not in map:
            map[char] = 0
        map[char] += 1

    tuples = list(map.items())
    # Sort alphabetically
    tuples.sort(key=lambda t: t[0])
    # Sort based on count
    tuples.sort(key=lambda t: t[1], reverse=True)
    return [letter for letter, _ in tuples]

#RUNTIME: O(n log n), where n is the number of unique characters
# ***** WRONG: max unique characters is 26 --> becomes O(l) where l is the length of word 
#SPACE: O(n), for the output and internal transitions and sorting
# ***** WRONG: O(n) is O(26) so this becomes O(1)

def run_tests():
    tests = [
        # Example from the book
        (
            "supercalifragilisticexpialidocious",
            ["i", "a", "c", "l", "s", "e", "o", "p", "r", "u", "d", "f", "g", "t", "x"],
        ),
        # Edge case - empty string
        ("", []),
        # Edge case - single character
        ("a", ["a"]),
        # Edge case - all same frequency
        ("abc", ["a", "b", "c"]),
        # Multiple frequencies with ties
        ("aabbbcccc", ["c", "b", "a"]),
        # All same character
        ("zzzzz", ["z"]),
        # Alternating characters
        ("ababab", ["a", "b"]),
        # Reverse alphabetical order but same frequency
        ("zyxwv", ["v", "w", "x", "y", "z"]),
        # Long string with many frequencies
        ("aaaaabbbbbbbcccccccccdddddddddddeeeeeeeeeeee", ["e", "d", "c", "b", "a"]),
    ]
    for word, want in tests:
        got1 = solution(word)
        assert (got1 == want), f"\nletter_occurrences({word}): got: {got1}, want: {want}\n"
        got2 = solution(word)
        assert (got2 == want), f"\nletter_occurrences_lambda({word}): got: {got2}, want: {want}\n"
        print("PASS")


run_tests()
