from functools import cache

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def count(n: int) -> int:
            digits = list(map(int, str(n)))

            @cache
            def dp(i, prev2, prev, tight, leading):
                if i == len(digits):
                    return 1, 0

                limit = digits[i] if tight else 9
                total_cnt = total_wav = 0

                check_wave = not leading and prev2 != -1 and prev != -1

                for d in range(limit + 1):
                    nt = tight and d == limit
                    nl = leading and d == 0

                    cnt, wav = dp(
                        i + 1,
                        prev,
                        -1 if nl else d,
                        nt,
                        nl
                    )

                    total_cnt += cnt
                    total_wav += wav

                    if check_wave and ((prev2 < prev > d) or (prev2 > prev < d)):
                        total_wav += cnt

                return total_cnt, total_wav

            return dp(0, -1, -1, True, True)[1]

        return count(num2) - count(num1 - 1)

if __name__ == "__main__":
    print(Solution().totalWaviness(120, 130))