from string import lowercase, uppercase

def caesar(s, n=1):
    """ simple caesar cipher
    """
    out = []
    for c in s:
        if c in uppercase:
            base = 'A'
        elif c in lowercase:
            base = 'a'
        else: # not a letter, just push it on
            out.append(c)
            continue
        out.append(chr((ord(c) - ord(base) + n) % 26 + ord(base)))
    return "".join(out)

def substitute(s, mapping):
    """ Substitute any keys in mapping with their value
        Keys must be single characters, or they will not be substituted
    """
    out = []
    for c in s:
        out.append(mapping.get(c, c))
    return "".join(out)

def join(itr, joiner=""):
    """ Sugar to join strings in a more sensible order
    """
    return joiner.join(itr)
