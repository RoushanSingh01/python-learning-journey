class Solution:
    def maximumGap(self, nums):
        if len(nums) < 2:
            return 0

        minimum = min(nums)
        maximum = max(nums)

        if minimum == maximum:
            return 0

        length = len(nums)

        bucket_size = max(1, (maximum - minimum) // (length - 1))
        bucket_count = (maximum - minimum) // bucket_size + 1

        buckets = [[None, None] for _ in range(bucket_count)]

        for num in nums:
            index = (num - minimum) // bucket_size

            if buckets[index][0] is None:
                buckets[index][0] = num
                buckets[index][1] = num
            else:
                buckets[index][0] = min(buckets[index][0], num)
                buckets[index][1] = max(buckets[index][1], num)

        max_gap = 0
        previous_max = buckets[0][1]

        for i in range(1, bucket_count):
            if buckets[i][0] is None:
                continue

            max_gap = max(max_gap, buckets[i][0] - previous_max)
            previous_max = buckets[i][1]

        return max_gap


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        [3, 6, 9, 1],
        [10],
        [1, 10000000],
        [1, 3, 100],
        [152, 3, 99, 42, 77],
    ]

    for nums in test_cases:
        result = solution.maximumGap(nums)

        print(f"Input: {nums}")
        print(f"Maximum Gap: {result}")
        print("-" * 40)