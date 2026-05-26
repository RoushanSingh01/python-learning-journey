class Solution:
    def maximumGap(self, nums):
        n = len(nums)

        if n < 2:
            return 0

        minimum = min(nums)
        maximum = max(nums)

        if minimum == maximum:
            return 0

        bucket_size = max(1, (maximum - minimum) // (n - 1))
        bucket_count = (maximum - minimum) // bucket_size + 1

        buckets = [[None, None] for _ in range(bucket_count)]

        for num in nums:
            index = (num - minimum) // bucket_size
            bucket = buckets[index]

            if bucket[0] is None:
                bucket[0] = num
                bucket[1] = num
            else:
                if num < bucket[0]:
                    bucket[0] = num

                if num > bucket[1]:
                    bucket[1] = num

        previous_max = None
        max_gap = 0

        for bucket_min, bucket_max in buckets:
            if bucket_min is None:
                continue

            if previous_max is not None:
                gap = bucket_min - previous_max

                if gap > max_gap:
                    max_gap = gap

            previous_max = bucket_max

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