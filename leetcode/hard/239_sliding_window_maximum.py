from collections import deque


class Solution:
    def maxSlidingWindow(self, nums, k):
        q = deque()
        res = []

        for i in range(len(nums)):
            while q and q[0] <= i - k:
                q.popleft()

            while q and nums[q[-1]] <= nums[i]:
                q.pop()

            q.append(i)

            if i >= k - 1:
                res.append(nums[q[0]])

        return res


if __name__ == "__main__":
    solution = Solution()

    print(solution.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
    print(solution.maxSlidingWindow([1], 1))
    print(solution.maxSlidingWindow([7, 2, 4], 2))