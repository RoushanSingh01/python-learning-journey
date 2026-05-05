class Solution:
    def letterCombinations(self, digits):
        dic = {
            '2': 'abc', '3': 'def', '4': 'ghi',
            '5': 'jkl', '6': 'mno', '7': 'pqrs',
            '8': 'tuv', '9': 'wxyz'
        }
        res = [""]

        for dig in digits:
            tmp = []
            for y in res:
                for x in dic[dig]:
                    tmp.append(y + x)
            res = tmp

        return res if any(res) else []


# ---------------- TEST CASES ----------------
if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        ("23", ["ad","ae","af","bd","be","bf","cd","ce","cf"]),
        ("", []),
        ("2", ["a","b","c"]),
        ("9", ["w","x","y","z"]),
        ("79", [
            "pw","px","py","pz",
            "qw","qx","qy","qz",
            "rw","rx","ry","rz",
            "sw","sx","sy","sz"
        ]),
        ("234", None),  # just checking length
    ]

    for digits, expected in test_cases:
        result = sol.letterCombinations(digits)

        print(f"Input: '{digits}'")
        print(f"Output: {result}")

        if expected is not None:
            print(f"Expected: {expected}")
            print("PASS" if sorted(result) == sorted(expected) else "FAIL")
        else:
            print(f"Length: {len(result)} (Expected: {3*3*3})")
            print("PASS" if len(result) == 27 else "FAIL")

        print("-" * 50)