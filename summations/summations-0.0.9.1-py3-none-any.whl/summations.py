"""Natural number lists with target sum.

Library to enumerate all natural number lists with a target sum.
"""

import doctest

def sum_len(target, length):
    """
    Generate every possible way of splitting a non-negative
    integer into the specified number of non-negative integer
    terms.

    >>> list(sum_len(2, 1))
    [(2,)]

    >>> sorted(list(sum_len(2, 3)))
    [(0, 0, 2), (0, 1, 1), (0, 2, 0), (1, 0, 1), (1, 1, 0), (2, 0, 0)]

    >>> sorted(list(sum_len(5, 3)))[:6]
    [(0, 0, 5), (0, 1, 4), (0, 2, 3), (0, 3, 2), (0, 4, 1), (0, 5, 0)]

    >>> sorted(list(sum_len(5, 3)))[6:12]
    [(1, 0, 4), (1, 1, 3), (1, 2, 2), (1, 3, 1), (1, 4, 0), (2, 0, 3)]
    """
    if length == 1:
        yield (target,)
    else:
        for i in range(target+1):
            for partial in sum_len(target-i, length-1):
                yield partial+(i,)

if __name__ == "__main__":
    doctest.testmod()
