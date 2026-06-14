from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


if __name__ == "__main__":
    solution = Solution()

    print(solution.isAnagram("anagram", "nagaram"))
    print(solution.isAnagram("rat", "car"))
    print(solution.isAnagram("rat", "car"))