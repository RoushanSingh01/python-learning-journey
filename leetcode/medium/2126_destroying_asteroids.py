from typing import List


class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()

        for asteroid in asteroids:
            if mass < asteroid:
                return False
            mass += asteroid

        return True


if __name__ == "__main__":
    sol = Solution()

    print(sol.asteroidsDestroyed(10, [3, 9, 19, 5, 21]))  # True
    print(sol.asteroidsDestroyed(5, [4, 9, 23, 4]))       # False

    # Additional Tests
    print(sol.asteroidsDestroyed(1, [1]))                 # True
    print(sol.asteroidsDestroyed(2, [1, 2, 1]))          # True
    print(sol.asteroidsDestroyed(3, [4]))                # False
    print(sol.asteroidsDestroyed(100, [1, 2, 3, 4]))     # True