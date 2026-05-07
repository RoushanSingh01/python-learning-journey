class Solution(object):
    def trap(self, height):

        if not height:
            return 0

        left = 0
        right = len(height) - 1

        left_max = 0
        right_max = 0

        trapped_water = 0

        while left < right:

            if height[left] < height[right]:

                if height[left] > left_max:
                    left_max = height[left]

                else:
                    trapped_water += (
                        left_max - height[left]
                    )

                left += 1

            else:

                if height[right] > right_max:
                    right_max = height[right]

                else:
                    trapped_water += (
                        right_max - height[right]
                    )

                right -= 1

        return trapped_water


def run_test(height, expected):
    result = Solution().trap(height)

    status = (
        "PASS"
        if result == expected
        else "FAIL"
    )

    print(
        f"{status} | height={height}, "
        f"expected={expected}, got={result}"
    )


if __name__ == "__main__":

    run_test(
        [0,1,0,2,1,0,1,3,2,1,2,1],
        6
    )

    run_test(
        [4,2,0,3,2,5],
        9
    )

    run_test(
        [],
        0
    )

    run_test(
        [1],
        0
    )

    run_test(
        [2,0,2],
        2
    )

    run_test(
        [3,0,1,3,0,5],
        8
    )