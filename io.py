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

def repl(prompt=">>> "):
    """ Start a repl using eval, call close_repl() to kill it
    """
    running = [True] # we need to make this a list because stupid scoping rules
    def close_repl():
        running[0] = False
    print "Starting repl, call close_repl() to exit"
    while running[0]:
        i = raw_input(prompt)
        try:
            print(eval(i))
        except:
            print "err:",i
