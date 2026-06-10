from heapq import heappush, heappop
from typing import List


class SparseTableRMQ:
    def __init__(self, data: List[int]):
        self.n = len(data)
        self.max_log = self.n.bit_length() + 1

        self.f_max = [[0] * self.max_log for _ in range(self.n)]
        self.f_min = [[0] * self.max_log for _ in range(self.n)]

        self.lg = [0] * (self.n + 1)

        for i in range(2, self.n + 1):
            self.lg[i] = self.lg[i >> 1] + 1

        for i in range(self.n):
            self.f_max[i][0] = data[i]
            self.f_min[i][0] = data[i]

        for j in range(1, self.max_log):
            limit = self.n - (1 << j) + 1

            for i in range(limit):
                self.f_max[i][j] = max(
                    self.f_max[i][j - 1],
                    self.f_max[i + (1 << (j - 1))][j - 1]
                )

                self.f_min[i][j] = min(
                    self.f_min[i][j - 1],
                    self.f_min[i + (1 << (j - 1))][j - 1]
                )

    def query_max(self, left: int, right: int) -> int:
        k = self.lg[right - left + 1]
        return max(
            self.f_max[left][k],
            self.f_max[right - (1 << k) + 1][k]
        )

    def query_min(self, left: int, right: int) -> int:
        k = self.lg[right - left + 1]
        return min(
            self.f_min[left][k],
            self.f_min[right - (1 << k) + 1][k]
        )


class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        n = len(nums)

        st = SparseTableRMQ(nums)

        query_max = st.query_max
        query_min = st.query_min

        heap = []

        for left in range(n):
            value = query_max(left, n - 1) - query_min(left, n - 1)
            heappush(heap, (-value, left, n - 1))

        answer = 0

        for _ in range(k):
            value, left, right = heappop(heap)

            answer += -value

            if right > left:
                new_value = (
                    query_max(left, right - 1)
                    - query_min(left, right - 1)
                )

                heappush(
                    heap,
                    (-new_value, left, right - 1)
                )

        return answer


if __name__ == "__main__":
    solution = Solution()

    print(solution.maxTotalValue([1, 3, 2], 2))
    print(solution.maxTotalValue([4, 7, 1, 9], 3))