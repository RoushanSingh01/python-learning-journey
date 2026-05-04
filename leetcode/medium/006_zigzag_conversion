class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        rows = [""] * numRows
        current_row = 0
        direction = 1

        for char in s:
            rows[current_row] += char

            if current_row == 0:
                direction = 1
            elif current_row == numRows - 1:
                direction = -1

            current_row += direction

        return "".join(rows)

# ---------------- TEST CASES ----------------
if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        ("PAYPALISHIRING", 3, "PAHNAPLSIIGYIR"),
        ("PAYPALISHIRING", 4, "PINALSIGYAHRPI"),
        ("A", 1, "A"),
        ("ABCD", 2, "ACBD"),
    ]

    for s, rows, expected in test_cases:
        result = sol.convert(s, rows)

        print(f"Input: {s}, rows={rows}")
        print(f"Output: {result} | Expected: {expected}")
        print("PASS" if result == expected else "FAIL")
        print("-" * 40)
