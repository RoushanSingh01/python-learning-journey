class Solution:
    def isPalindrome(self, s):
        left = 0
        right = len(s) - 1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1

            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True


def run_tests():
    solution = Solution()

    assert solution.isPalindrome("A man, a plan, a canal: Panama")

    assert not solution.isPalindrome("race a car")

    assert solution.isPalindrome(" ")

    assert solution.isPalindrome("")

    assert solution.isPalindrome("0P0")

    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
