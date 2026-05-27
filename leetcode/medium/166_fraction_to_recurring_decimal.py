class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:

        if numerator == 0:
            return "0"

        result = []

        if numerator * denominator < 0:
            result.append("-")

        numerator = abs(numerator)
        denominator = abs(denominator)

        result.append(str(numerator // denominator))

        remainder = numerator % denominator

        if remainder == 0:
            return "".join(result)

        result.append(".")

        seen_remainders = {}

        while remainder:

            if remainder in seen_remainders:
                repeat_index = seen_remainders[remainder]
                result.insert(repeat_index, "(")
                result.append(")")
                break

            seen_remainders[remainder] = len(result)

            remainder *= 10

            result.append(str(remainder // denominator))

            remainder %= denominator

        return "".join(result)


sol = Solution()

print(sol.fractionToDecimal(1, 2))
print(sol.fractionToDecimal(2, 1))
print(sol.fractionToDecimal(4, 333))
print(sol.fractionToDecimal(1, 6))
print(sol.fractionToDecimal(-50, 8))
print(sol.fractionToDecimal(7, -12))
print(sol.fractionToDecimal(0, 5))