from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        target_count = Counter(t)
        window_count = {}

        required = len(target_count)
        formed = 0

        left = 0
        min_length = float("inf")
        result = (0, 0)

        for right in range(len(s)):
            char = s[right]

            window_count[char] = window_count.get(char, 0) + 1

            if char in target_count and window_count[char] == target_count[char]:
                formed += 1

            while formed == required:
                if right - left + 1 < min_length:
                    min_length = right - left + 1
                    result = (left, right)

                left_char = s[left]

                window_count[left_char] -= 1

                if (
                    left_char in target_count
                    and window_count[left_char] < target_count[left_char]
                ):
                    formed -= 1

                left += 1

        if min_length == float("inf"):
            return ""

        start, end = result
        return s[start : end + 1]


def run_test(s, t, expected):
    result = Solution().minWindow(s, t)

    if result == expected:
        print(f"PASS | s='{s}', t='{t}' -> '{result}'")
    else:
        print(f"FAIL | s='{s}', t='{t}' -> got '{result}', expected '{expected}'")


if __name__ == "__main__":
    run_test("ADOBECODEBANC", "ABC", "BANC")
    run_test("a", "a", "a")
    run_test("a", "aa", "")
    run_test("aa", "aa", "aa")
    run_test("ab", "b", "b")
