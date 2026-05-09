# 060_permutation_sequence.py

import math


class Solution:
    def getPermutation(self, n, k):
        nums = [str(i) for i in range(1, n + 1)]

        k -= 1
        result = []

        for i in range(n, 0, -1):
            fact = math.factorial(i - 1)

            index = k // fact

            result.append(nums.pop(index))

            k %= fact

        return "".join(result)


def run_test(n, k, expected):
    result = Solution().getPermutation(n, k)

    status = "PASS" if result == expected else "FAIL"

    print(f"{status} | n={n}, k={k}")
    print(f"expected={expected}")
    print(f"got     ={result}")
    print()


# Test Cases
run_test(3, 3, "213")
run_test(4, 9, "2314")
run_test(3, 1, "123")
run_test(3, 6, "321")
run_test(1, 1, "1")