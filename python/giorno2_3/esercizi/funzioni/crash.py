def factorial(n):
    """Calculate the factorial of the given number"""
    # FIXME: this code has a bug!
    if n > 1:
        return n * factorial(n)
    else:
        return 1


assert factorial(5) == 120
