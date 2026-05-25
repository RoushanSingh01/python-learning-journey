class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)

        if s[-1] == "1":
            return False

        q = [0]
        farthest = 0

        for i in q:
            start = max(i + minJump, farthest)
            end = min(i + maxJump + 1, n)

            for j in range(start, end):
                if s[j] == "0":
                    if j == n - 1:
                        return True

                    q.append(j)

            farthest = end

        return n == 1


def run_tests():
    sol = Solution()

    test_cases = [
        ("011010", 2, 3, True),
        ("01101110", 2, 3, False),
        ("0000000", 2, 5, True),
        ("00000", 4, 4, True),
        ("01", 1, 1, False),
        ("0", 1, 1, True),
    ]

    for idx, (s, mn, mx, expected) in enumerate(test_cases, 1):
        result = sol.canReach(s, mn, mx)

        print(f"Test {idx}")
        print(f"Input: s={s}, minJump={mn}, maxJump={mx}")
        print(f"Expected: {expected}")
        print(f"Output:   {result}")
        print(f"Passed:   {result == expected}")
        print("-" * 50)


if __name__ == "__main__":
    run_tests()
