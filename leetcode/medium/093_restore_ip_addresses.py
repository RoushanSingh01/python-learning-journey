from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []

        def backtrack(start: int, parts: list[str]) -> None:
            if len(parts) == 4:
                if start == len(s):
                    result.append(".".join(parts))
                return

            for length in range(1, 4):
                if start + length > len(s):
                    break

                segment = s[start : start + length]

                if segment.startswith("0") and len(segment) > 1:
                    continue

                if int(segment) > 255:
                    continue

                parts.append(segment)
                backtrack(start + length, parts)
                parts.pop()

        backtrack(0, [])

        return result


def run_tests():
    solution = Solution()

    test_cases = [
        ("25525511135", ["255.255.11.135", "255.255.111.35"]),
        ("0000", ["0.0.0.0"]),
        ("101023", ["1.0.10.23", "1.0.102.3", "10.1.0.23", "10.10.2.3", "101.0.2.3"]),
    ]

    for s, expected in test_cases:
        result = sorted(solution.restoreIpAddresses(s))
        expected = sorted(expected)

        print(
            f"Input: {s}\n"
            f"Expected: {expected}\n"
            f"Got: {result}\n"
            f"Passed: {result == expected}\n"
        )


if __name__ == "__main__":
    run_tests()
