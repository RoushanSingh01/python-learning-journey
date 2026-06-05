"""Generate prime numbers using the Sieve of Eratosthenes."""


def primes(limit):
    """Return all prime numbers up to the limit."""
    if limit < 2:
        return []

    sieve = [True] * (limit + 1)

    sieve[0] = False
    sieve[1] = False

    for number in range(2, int(limit ** 0.5) + 1):
        if sieve[number]:
            for multiple in range(
                number * number,
                limit + 1,
                number,
            ):
                sieve[multiple] = False

    return [
        number
        for number in range(2, limit + 1)
        if sieve[number]
    ]