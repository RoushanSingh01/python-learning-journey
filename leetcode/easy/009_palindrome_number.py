class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers are not palindrome
        if x < 0:
            return False

        original = x
        reverse = 0

        while x != 0:
            digit = x % 10
            reverse = reverse * 10 + digit
            x //= 10

        return original == reverse


# ---- test cases ----
s = Solution()
print(s.isPalindrome(121))  # expected True
print(s.isPalindrome(-121))  # expected False
print(s.isPalindrome(10))  # expected False
