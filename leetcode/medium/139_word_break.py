class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        words = set(wordDict)
        reachable = [0]

        min_len = min(map(len, words))
        max_len = max(map(len, words))

        for end in range(1, len(s) + 1):
            for start in reachable:
                length = end - start

                if length < min_len or length > max_len:
                    continue

                if s[start:end] in words:
                    reachable.append(end)

                    if end == len(s):
                        return True

                    break

        return False


if __name__ == "__main__":
    solution = Solution()

    s = "leetcode"
    wordDict = ["leet", "code"]

    result = solution.wordBreak(s, wordDict)

    print(result)