class Solution:
    def reverseBits(self, n):
        return int(bin(n)[2:].zfill(32)[::-1], 2)


def run_tests():
    solution = Solution()

    test_cases = [
        (43261596, 964176192),
        (4294967293, 3221225471),
        (0, 0),
        (1, 2147483648),
    ]

    for n, expected in test_cases:
        result = solution.reverseBits(n)
        assert result == expected, (
            f"Failed: reverseBits({n}) = {result}, expected {expected}"
        )

    print("All tests passed!")


if __name__ == "__main__":
    run_tests()