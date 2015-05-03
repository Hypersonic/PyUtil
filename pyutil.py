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

def join(s, joiner=""):
    """ Sugar to join strings in a more sensible order
    """
    return joiner.join(s)

def load_file(filename):
    """ Open filename and return its contents as a string
    """
    with open(filename) as f:
        return f.read()

def save_file(filename, contents):
    """ Open filename and dump contents to it.
        If the file exists, it is overwritten
    """
    with open(filename, 'w') as f:
        f.write(contents)
