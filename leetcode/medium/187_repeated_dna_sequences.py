from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen = set()
        repeated = set()

        for i in range(len(s) - 9):
            seq = s[i : i + 10]

            if seq in seen:
                repeated.add(seq)
            else:
                seen.add(seq)

        return list(repeated)


if __name__ == "__main__":
    sol = Solution()

    print(sol.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
    # ['AAAAACCCCC', 'CCCCCAAAAA']

    print(sol.findRepeatedDnaSequences("AAAAAAAAAAAAA"))
    # ['AAAAAAAAAA']

    print(sol.findRepeatedDnaSequences("ACGTACGTAC"))
    # []

    print(sol.findRepeatedDnaSequences("AAAAAAAAAAA"))
    # ['AAAAAAAAAA']

    print(sol.findRepeatedDnaSequences("A"))
    # []

    print(sol.findRepeatedDnaSequences(""))
    # []
