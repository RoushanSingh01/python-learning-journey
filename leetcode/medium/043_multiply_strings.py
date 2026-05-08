class Solution:
    def multiply(self, num1, num2):

        digit_map = {
            str(i): i
            for i in range(10)
        }

        length1 = len(num1) - 1
        length2 = len(num2) - 1

        first_number = sum([
            digit_map[digit] * (10 ** (length1 - index))
            for index, digit in enumerate(num1)
        ])

        second_number = sum([
            digit_map[digit] * (10 ** (length2 - index))
            for index, digit in enumerate(num2)
        ])

        return str(first_number * second_number)


def run_test(num1, num2, expected):
    result = Solution().multiply(num1, num2)

    status = (
        "PASS"
        if result == expected
        else "FAIL"
    )

    print(
        f"{status} | num1={num1}, "
        f"num2={num2}, expected={expected}, got={result}"
    )


if __name__ == "__main__":

    run_test("2", "3", "6")

    run_test("123", "456", "56088")

    run_test("0", "52", "0")

    run_test("999", "999", "998001")

    run_test("1", "99999", "99999")

    run_test("123456789", "987654321", "121932631112635269")