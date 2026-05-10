class Solution:
    def addBinary(self, a: str, b: str) -> str:

        i, j = len(a) - 1, len(b) - 1
        carry = 0
        result = []

        while i >= 0 or j >= 0 or carry:
            total = carry

            if i >= 0:
                total += ord(a[i]) - ord("0")
                i -= 1

            if j >= 0:
                total += ord(b[j]) - ord("0")
                j -= 1

            result.append(str(total % 2))
            carry = total // 2

        return "".join(result[::-1])


def run_test(a, b, expected):
    result = Solution().addBinary(a, b)

    status = "PASS" if result == expected else "FAIL"

    print(f"{status} | expected={expected}, got={result}")


# Test Cases
run_test("11", "1", "100")

run_test("1010", "1011", "10101")

run_test("0", "0", "0")

run_test("1111", "1111", "11110")

run_test("1", "111", "1000")
