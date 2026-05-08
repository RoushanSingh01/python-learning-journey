class Solution:
    def isMatch(self, s, p):

        string_pointer = 0
        pattern_pointer = 0

        match_index = 0
        star_index = -1

        while string_pointer < len(s):
            if pattern_pointer < len(p) and (
                s[string_pointer] == p[pattern_pointer] or p[pattern_pointer] == "?"
            ):
                string_pointer += 1
                pattern_pointer += 1

            elif pattern_pointer < len(p) and p[pattern_pointer] == "*":
                star_index = pattern_pointer
                match_index = string_pointer
                pattern_pointer += 1

            elif star_index != -1:
                pattern_pointer = star_index + 1
                match_index += 1
                string_pointer = match_index

            else:
                return False

        while pattern_pointer < len(p) and p[pattern_pointer] == "*":
            pattern_pointer += 1

        return pattern_pointer == len(p)


def run_test(s, p, expected):
    result = Solution().isMatch(s, p)

    status = "PASS" if result == expected else "FAIL"

    print(f"{status} | s={s}, p={p}, expected={expected}, got={result}")


if __name__ == "__main__":
    run_test("aa", "a", False)

    run_test("aa", "*", True)

    run_test("cb", "?a", False)

    run_test("adceb", "*a*b", True)

    run_test("acdcb", "a*c?b", False)

    run_test("", "*", True)

    run_test("abcabczzzde", "*abc???de*", True)
