from itertools import izip, combinations
from string import printable
from chain import *
from iteration import *

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

