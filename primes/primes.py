"""Return count number of prime numbers, starting at 2.

For example::

    >>> primes(0)
    []

    >>> primes(1)
    [2]

    >>> primes(5)
    [2, 3, 5, 7, 11]

"""


def primes(count):
    """Return count number of prime numbers, starting at 2."""
    primes = [2]
    i = 3
    if count < 1:
        return []
    elif count == 1:
        return primes
    else:
        while len(primes) < count:
            for num in range(2, i):
                prime = True
                if i % num == 0:
                    prime = False
                    break
                else:
                    continue
            if prime == True:
                primes.append(i)

            i += 1

    return primes

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. GREAT WORK!\n"
