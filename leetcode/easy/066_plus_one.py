class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits

            digits[i] = 0

        return [1] + digits


def run_test(digits, expected):
    result = Solution().plusOne(digits[:])

    status = "PASS" if result == expected else "FAIL"

    print(f"{status} | expected={expected}, got={result}")


# Test Cases
run_test([1, 2, 3], [1, 2, 4])

run_test([4, 3, 2, 1], [4, 3, 2, 2])

run_test([9], [1, 0])

run_test([9, 9, 9], [1, 0, 0, 0])

run_test([1, 9, 9], [2, 0, 0])
