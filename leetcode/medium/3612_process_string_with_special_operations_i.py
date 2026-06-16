class Solution:
    def processStr(self, s: str) -> str:
        result = []

        for c in s:
            if c.isalpha():
                result.append(c)

            elif c == "*" and result:
                result.pop()

            elif c == "#":
                result.extend(result)

            elif c == "%":
                result.reverse()

        return "".join(result)


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        "a#b%*",
        "abc#",
        "abc%",
        "abc*",
        "a#",
        "a##",
    ]

    for s in test_cases:
        print(f"Input : {s}")
        print(f"Output: {solution.processStr(s)}")
        print()