def fibonacci(n):
    """
    This function produces the nth value in the fibonacci sequence
    using range to iterate over the sequence
    """
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


def lucas(n):
    """
    This function produces the nth value in the lucas sequence
    using range to iterate over the sequence
    """
    a, b = 2, 1
    for i in range(n):
        a, b = b, a + b
    return a


def sum_series(n):
    """
    This function adds the sum of a series of numbers. For parameters,
    it takes one required argument and two option ones.
    """
    
    pass



