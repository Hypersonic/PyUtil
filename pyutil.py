from itertools import izip, combinations
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

def brute_force(up_to_len, alphabet=printable):
    """ Generate all combinations of an alphabet,
        to up_to_len long combinations

        Returns a generator
    """
    for i in xrange(up_to_len + 1):
        for x in combinations(alphabet, i):
            yield join(x, "")


class Chain(object):
    """ Returns a D-style UFCS-able object
        Caveat: You must call .data on the last element
        of the chain to get the output
    """
    def __init__(self, data):
        self.data = data
    def __getattr__(self, func_name):
        try:
            # If the function exists as a member function, use that
            if func_name in self.data.__class__.__dict__:
                func = self.data.__class__.__dict__[func_name]
            # Otherwise, use it as the first argument to a global function
            else:
                func = eval(func_name) # we have to use eval for this q.q
            return lambda *args, **kwargs: Chain(func(self.data, *args, **kwargs))
        except NameError, e:
            return getattr(self.data, func_name)
    def __repr__(self):
        return 'Chain(' + repr(self.data) + ')'
    def __str__(self):
        return str(self.data)
    def __iter__(self):
        """ Return an iterator over the data in a chain
            The Chain-ness is transitive, meaning all elements inside the chain
            get wrapped in a Chain
        """
        return (Chain(x) for x in self.data)

def mapR(itr, func):
    """ Same as `map`, but with the arguments reversed for use in a `Chain`
    """
    return [func(i) for i in itr]

def imapR(itr, func):
    """ Same as `imap`, but with the arguments reversed for use in a `Chain`
    """
    return (func(i) for i in itr)

def filterR(itr, pred):
    """ Same as `filter`, but with the arguments reversed for use in a `Chain`
    """
    return [i for i in itr if pred(i)]

def ifilterR(itr, pred):
    """ Same as `ifilter`, but with the arguments reversed for use in a `Chain`
    """
    return (i for i in itr if pred(i))
