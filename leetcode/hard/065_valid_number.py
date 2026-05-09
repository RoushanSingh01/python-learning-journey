# 065_valid_number.py

class Solution:
    def isNumber(self, s):
        s = s.strip()

        pointSeen = False
        eSeen = False
        numberSeen = False
        numberAfterE = True

        for i, c in enumerate(s):

            if "0" <= c <= "9":
                numberSeen = True
                numberAfterE = True

            elif c == ".":

                if pointSeen or eSeen:
                    return False

                pointSeen = True

            elif c in "eE":

                if eSeen or not numberSeen:
                    return False

                eSeen = True
                numberAfterE = False

            elif c in "+-":

                if i > 0 and s[i - 1] not in "eE":
                    return False

            else:
                return False

        return numberSeen and numberAfterE


def run_test(s, expected):
    result = Solution().isNumber(s)

    status = "PASS" if result == expected else "FAIL"

    print(f'{status} | s="{s}"')
    print(f"expected={expected}")
    print(f"got     ={result}")
    print()


# Valid numbers
run_test("0", True)
run_test(" 0.1 ", True)
run_test("2e10", True)
run_test("-90E3", True)
run_test("3.", True)
run_test("+.8", True)
run_test("53.5e93", True)

# Invalid numbers
run_test("abc", False)
run_test("1a", False)
run_test("1e", False)
run_test("e3", False)
run_test("99e2.5", False)
run_test("--6", False)
run_test("-+3", False)
run_test("95a54e53", False)
run_test("inf", False)