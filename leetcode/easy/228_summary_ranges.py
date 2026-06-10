from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        def format_range(start: int, end: int) -> str:
            return str(nums[start]) if start == end else f"{nums[start]}->{nums[end]}"

        index = 0
        length = len(nums)
        ranges = []

        while index < length:
            end = index

            while end + 1 < length and nums[end + 1] == nums[end] + 1:
                end += 1

            ranges.append(format_range(index, end))
            index = end + 1

        return ranges


if __name__ == "__main__":
    solution = Solution()

    print(solution.summaryRanges([0, 1, 2, 4, 5, 7]))
    print(solution.summaryRanges([0, 2, 3, 4, 6, 8, 9]))
    print(solution.summaryRanges([]))