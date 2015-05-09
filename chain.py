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

def reduceR(itr, func, initial=0):
    """ Same as `reduce`, but with the arguments reversed
    (sequence first) for use in a `Chain`
    """
    return reduce(func, itr, intial)
