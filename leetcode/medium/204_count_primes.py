class Solution:
    def countPrimes(self, n):
        if n < 3:
            return 0

        prime = [True] * n
        prime[0] = prime[1] = False

        for i in range(2, int(n ** 0.5) + 1):
            if prime[i]:
                prime[i * i:n:i] = [False] * len(
                    prime[i * i:n:i]
                )

        return sum(prime)


if __name__ == "__main__":
    sol = Solution()

    test_cases = [10, 0, 1, 2, 100]

    for n in test_cases:
        print(f"n = {n}")
        print("count =", sol.countPrimes(n))
        print()