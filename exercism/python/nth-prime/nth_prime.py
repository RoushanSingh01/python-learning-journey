"""Find the nth prime number."""


def prime(number):
    """Return the nth prime number."""

    if number == 0:
        raise ValueError("there is no zeroth prime")

    candidate = 1
    primes_found = 0

    while primes_found < number:

        candidate += 1
        is_prime = True

        for divisor in range(2, int(candidate ** 0.5) + 1):

            if candidate % divisor == 0:
                is_prime = False
                break

        if is_prime:
            primes_found += 1

    return candidate