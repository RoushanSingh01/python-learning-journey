class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1) < len(word2):
            word1, word2 = word2, word1

        previous_row = list(range(len(word2) + 1))

        for i in range(1, len(word1) + 1):
            current_row = [i] + [0] * len(word2)

            for j in range(1, len(word2) + 1):
                if word1[i - 1] == word2[j - 1]:
                    current_row[j] = previous_row[j - 1]
                else:
                    current_row[j] = 1 + min(
                        previous_row[j],  # delete
                        current_row[j - 1],  # insert
                        previous_row[j - 1],  # replace
                    )

            previous_row = current_row

        return previous_row[-1]


def run_test(word1, word2, expected):
    result = Solution().minDistance(word1, word2)

    if result == expected:
        print(f"PASS | word1='{word1}', word2='{word2}' -> {result}")
    else:
        print(
            f"FAIL | word1='{word1}', word2='{word2}' "
            f"-> got {result}, expected {expected}"
        )


if __name__ == "__main__":
    run_test("horse", "ros", 3)
    run_test("intention", "execution", 5)
    run_test("", "", 0)
    run_test("abc", "", 3)
    run_test("", "abc", 3)
    run_test("kitten", "sitting", 3)
