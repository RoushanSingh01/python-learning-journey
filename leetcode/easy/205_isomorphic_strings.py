class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_s = [-1] * 256
        map_t = [-1] * 256

        for i in range(len(s)):
            char_s = ord(s[i])
            char_t = ord(t[i])

            if map_s[char_s] != map_t[char_t]:
                return False

            map_s[char_s] = i
            map_t[char_t] = i

        return True


if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        ("egg", "add"),
        ("foo", "bar"),
        ("paper", "title"),
        ("badc", "baba"),
        ("ab", "aa"),
    ]

    for s, t in test_cases:
        print(f"s = '{s}', t = '{t}'")
        print("Result:", sol.isIsomorphic(s, t))
        print()