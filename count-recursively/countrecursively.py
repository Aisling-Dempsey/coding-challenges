"""Count items in a list recursively.

For example:

        >>> count_recursively([])
        0

        >>> count_recursively([1, 2, 3])
        3

"""


def count_recursively(lst):
    """Return number of items in a list, using recursion."""
#     base case
    while lst:
        return count_recursively(lst[1:]) + 1
    return 0

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. GO YOU!\n"
