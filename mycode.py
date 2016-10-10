"""

This is an example python file

"""

def adder(x, y):
    """Adds x and y

    >>> adder(2, 2)
    4
    
    """
    return x + y

if __name__ == '__main__':
    import doctest
    doctest.testmod()
