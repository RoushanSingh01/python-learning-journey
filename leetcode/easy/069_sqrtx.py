class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        answer = 0

        while left <= right:
            mid = (left + right) // 2

            if mid * mid <= x:
                answer = mid
                left = mid + 1
            else:
                right = mid - 1

        return answer


def run_test(x, expected):
    result = Solution().mySqrt(x)

    if result == expected:
        print(f"PASS | x={x} -> {result}")
    else:
        print(f"FAIL | x={x} -> got {result}, expected {expected}")


if __name__ == "__main__":
    run_test(4, 2)
    run_test(8, 2)
    run_test(0, 0)
    run_test(1, 1)
    run_test(16, 4)
    run_test(2147395599, 46339)