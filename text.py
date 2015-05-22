from string import lowercase, uppercase

def caesar(s, n=1):
    """ simple caesar cipher
    """
    out = ""
    for c in s:
        if c in uppercase:
            base = 'A'
        elif c in lowercase:
            base = 'a'
        else: # not a letter, just push it on
            out += c
            continue
        out += chr((ord(c) - ord(base) + n) % 26 + ord(base))
    return out

def substitute(s, mapping):
    out = ""
    for c in s:
        out += mapping.get(c, c)
    return out

def join(itr, joiner=""):
    """ Sugar to join strings in a more sensible order
    """
    return joiner.join(itr)
