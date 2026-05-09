import itertools


class Solution:
    def getPermutation(self, n, k):
        p = itertools.permutations(range(1, n + 1))

        for _ in range(k):
            res = next(p)

        return "".join([str(i) for i in res])


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