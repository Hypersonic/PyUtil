from itertools import izip, combinations
from text import join
from string import printable

def groups_of(itr, n=8):
    """ Return groups of n consecutive elements from itr
        n defaults to 8

        Returns a generator
    """
    return izip(*[iter(itr)]*n)

def every_nth(itr, n=8, offset=0):
    """ Return every nth element of itr, starting with offset
        n defaults to 8, offset 0

        offset must be less than n

        Returns a generator
    """
    return (group[offset] for group in groups_of(itr, n))

def window(itr, n=8):
    """ Returns a sliding window over itr, giving access to
        n consecutive elements at a time.

        n defaults to 8

        Returns a generator
    """
    prevs = []
    for item in itr:
        prevs.append(item)
        if len(prevs) == n:
            yield prevs
            prevs = prevs[1:]

def take(itr, n):
    """ Take off the first n items of an iterator, and return them.

        Returns a list
    """
    return [b for a,b in zip(range(n), itr)]

def brute_force(up_to_len, alphabet=printable):
    """ Generate all combinations of an alphabet,
        to up_to_len long combinations

        Returns a generator
    """
    for i in xrange(up_to_len + 1):
        for x in combinations(alphabet, i):
            yield join(x, "")
