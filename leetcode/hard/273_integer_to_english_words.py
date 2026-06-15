
class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        lt20 = [
            "",
            "One",
            "Two",
            "Three",
            "Four",
            "Five",
            "Six",
            "Seven",
            "Eight",
            "Nine",
            "Ten",
            "Eleven",
            "Twelve",
            "Thirteen",
            "Fourteen",
            "Fifteen",
            "Sixteen",
            "Seventeen",
            "Eighteen",
            "Nineteen",
        ]

        tens = [
            "",
            "Ten",
            "Twenty",
            "Thirty",
            "Forty",
            "Fifty",
            "Sixty",
            "Seventy",
            "Eighty",
            "Ninety",
        ]

        thousands = ["Billion", "Million", "Thousand", ""]

        def transfer(num):
            if num == 0:
                return ""
            if num < 20:
                return lt20[num] + " "
            if num < 100:
                return tens[num // 10] + " " + transfer(num % 10)
            return lt20[num // 100] + " Hundred " + transfer(num % 100)

        res = []

        i, j = 1000000000, 0

        while i > 0:
            if num // i != 0:
                res.append(transfer(num // i))
                res.append(thousands[j])
                res.append(" ")
                num %= i

            j += 1
            i //= 1000

        return "".join(res).strip()


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        123,
        12345,
        1234567,
        1000000,
        2147483647,
        0,
    ]

    for num in test_cases:
        print(f"Input : {num}")
        print(f"Output: {solution.numberToWords(num)}")
        print()