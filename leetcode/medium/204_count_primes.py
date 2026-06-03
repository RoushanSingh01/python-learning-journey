class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0

        sieve = [True] * n
        sieve[0] = sieve[1] = False

        limit = int(n ** 0.5) + 1

        for i in range(3, limit, 2):
            if sieve[i]:
                sieve[i * i:n:2 * i] = [False] * len(
                    sieve[i * i:n:2 * i]
                )

        count = 1  # Prime number 2

        for i in range(3, n, 2):
            if sieve[i]:
                count += 1

        return count


if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        0,
        1,
        2,
        10,
        100,
        1000,
    ]

    for n in test_cases:
        print(f"Primes less than {n}: {sol.countPrimes(n)}")