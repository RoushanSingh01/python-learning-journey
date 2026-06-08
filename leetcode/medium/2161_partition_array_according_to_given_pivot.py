from typing import List


class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left = []
        right = []
        count = 0

        for num in nums:
            if num < pivot:
                left.append(num)
            elif num > pivot:
                right.append(num)
            else:
                count += 1

        return left + [pivot] * count + right


if __name__ == "__main__":
    solution = Solution()

    print(solution.pivotArray([9, 12, 5, 10, 14, 3, 10], 10))
    print(solution.pivotArray([-3, 4, 3, 2], 2))