from itertools import izip

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
