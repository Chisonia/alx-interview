#!/usr/bin/python3
'''Game module'''


def sieve_of_eratosthenes(n):
    """Generate a list of primes up
    to n using the Sieve of Eratosthenes."""
    is_prime = [True] * (n + 1)
    is_prime[0], is_prime[1] = False, False

    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    primes = []
    for i in range(n + 1):
        if is_prime[i]:
            primes.append(i)
    return primes


def isWinner(x, nums):
    """Determine who wins the most rounds."""
    if not nums or x <= 0:
        return None

    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)

    # Precompute the number of primes up to each number
    prime_count = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_count[i] = prime_count[i - 1] + (1 if i in primes else 0)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        # Total number of primes up to n
        primes_up_to_n = prime_count[n]

        # If the number of primes is odd, Maria wins; otherwise, Ben wins
        if primes_up_to_n % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
