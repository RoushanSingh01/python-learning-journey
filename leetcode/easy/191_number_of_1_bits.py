class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0

        while n:
            n &= n - 1
            count += 1

        return count


def run_tests():
    solution = Solution()

    test_cases = [
        (0b00000000000000000000000000001011, 3),
        (0b00000000000000000000000010000000, 1),
        (0b11111111111111111111111111111101, 31),
        (0, 0),
    ]

    for n, expected in test_cases:
        result = solution.hammingWeight(n)
        assert result == expected, (
            f"Failed: hammingWeight({n}) = {result}, expected {expected}"
        )

    print("All tests passed!")


if __name__ == "__main__":
    run_tests()