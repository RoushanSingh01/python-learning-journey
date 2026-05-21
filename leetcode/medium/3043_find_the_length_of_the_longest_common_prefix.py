from typing import List


class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefixes = set()

        for num in arr1:
            while num:
                prefixes.add(num)
                num //= 10

        ans = 0

        for num in arr2:
            while num:
                if num in prefixes:
                    ans = max(ans, len(str(num)))
                    break
                num //= 10

        return ans


if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        ([1, 10, 100], [1000], 3),
        ([1, 2, 3], [4, 4, 4], 0),
        ([12345, 56789], [123, 56], 3),
        ([5655359], [56554], 4),
        ([12, 123, 1234], [12345], 4),
    ]

    for i, (arr1, arr2, expected) in enumerate(test_cases, 1):
        result = sol.longestCommonPrefix(arr1, arr2)

        print(f"Test Case {i}")
        print(f"arr1 = {arr1}")
        print(f"arr2 = {arr2}")
        print(f"Expected = {expected}")
        print(f"Got = {result}")
        print("PASS" if result == expected else "FAIL")
        print("-" * 40)