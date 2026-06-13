from string import ascii_lowercase


class Solution:
    def mapWordWeights(self, words, weights):
        mp = dict(zip(ascii_lowercase, weights))
        res = []

        for w in words:
            s = 0
            for c in w:
                s += mp[c]

            res.append(ascii_lowercase[(25 - s) % 26])

        return "".join(res)


if __name__ == "__main__":
    words = ["abcd", "def", "xyz"]
    weights = list(range(1, 27))

    solution = Solution()
    print(solution.mapWordWeights(words, weights))