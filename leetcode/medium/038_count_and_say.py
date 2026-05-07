class Solution:
    def countAndSay(self, n):
        current = "1"

        for _ in range(n - 1):
            temp = ""
            count = 1

            for index, char in enumerate(current):
                if index > 0 and current[index - 1] == char:
                    count += 1

                elif index > 0:
                    temp += str(count) + current[index - 1]
                    count = 1

                if index == len(current) - 1:
                    temp += str(count) + current[index]

            current = temp

        return current


def run_test(n, expected):
    result = Solution().countAndSay(n)
    status = "PASS" if result == expected else "FAIL"
    print(f"{status} | n={n}, expected={expected}, got={result}")


if __name__ == "__main__":
    run_test(1, "1")
    run_test(2, "11")
    run_test(3, "21")
    run_test(4, "1211")
    run_test(5, "111221")
    run_test(6, "312211")
