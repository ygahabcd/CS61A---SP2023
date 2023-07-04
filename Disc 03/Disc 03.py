"""
Q1: Warm Up: Recursive Multiplication
Write a function that takes two numbers m and n and returns their product. Assume m and n are positive integers.
    Use recursion, not mul or *.
    Hint: 5 * 3 = 5 + (5 * 2) = 5 + 5 + (5 * 1).
    For the base case, what is the simplest possible input for multiply?
    For the recursive case, what does calling multiply(m - 1, n) do? What does calling multiply(m, n - 1) do?
    Do we prefer one over the other?
"""


def multiply(m, n):
    """ Takes two positive integers and returns their product using recursion.
    >>> multiply(5, 3)
    15
    """
    "*** YOUR CODE HERE ***"
    if n == 0:
        return 0
    elif n == 1:
        return m
    elif n > 1:
        return m + multiply(m, n - 1)


"""
Q2: Recursion Environment Diagram
Draw an environment diagram for the following code:
"""


def rec(x, y):
    """
    >>> rec(3, 2)
    9
    """
    if y > 0:
        return x * rec(x, y - 1)
    return 1


"""
Q3: Find the Bug
Find the bug with this recursive function.
"""


def skip_mul(n):
    """Return the product of n * (n - 2) * (n - 4) * ...

    >>> skip_mul(5) # 5 * 3 * 1
    15
    >>> skip_mul(8) # 8 * 6 * 4 * 2
    384
    """
    if n == 2:
        return 2
    elif n < 0:
        return 1
    else:
        return n * skip_mul(n - 2)


"""
Q4: Is Prime
Write a function is_prime that takes a single argument n and returns True if n is a prime number and False otherwise.
Assume n > 1. We implemented this in Discussion 1 iteratively, now time to do it recursively!

Hint: You will need a helper function! Remember helper functions are nested functions that are useful if you need to 
keep track of more variables than the given parameters, or if you need to change the value of the input.
"""


def is_prime(n):
    """Returns True if n is a prime number and False otherwise.

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    "*** YOUR CODE HERE ***"

    def helper(n, m):
        if m == 1:
            return True
        elif n % m == 0:
            return False
        else:
            return helper(n, m - 1)

    return helper(n, n - 1)


"""
Q5: Recursive Hailstone
Recall the hailstone function from Homework 1. First, pick a positive integer n as the start. If n is even, 
divide it by 2. If n is odd, multiply it by 3 and add 1. Repeat this process until n is 1. Write a recursive version of 
hailstone that prints out the values of the sequence and returns the number of steps.

Hint: When taking the recursive leap of faith, consider both the return value and side effect of this function.
"""


def hailstone(n):
    """Print out the hailstone sequence starting at n, and return the number of elements in the sequence.
    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    >>> b = hailstone(1)
    1
    >>> b
    1
    """
    "*** YOUR CODE HERE ***"
    print(int(n))
    if n == 1:
        return 1
    elif n % 2 == 0:
        return hailstone(n / 2) + 1
    else:
        return hailstone(n * 3 + 1) + 1


"""            
Q6: Merge Numbers
Write a procedure merge(n1, n2) which takes numbers with digits in decreasing order and returns a single number with all 
of the digits of the two, in decreasing order. Any number merged with 0 will be that number (treat 0 as having no 
digits). Use recursion.

Hint: If you can figure out which number has the smallest digit out of both, then we know that the resulting number will 
have that smallest digit, followed by the merge of the two numbers with the smallest digit removed.
"""


def merge(n1, n2):
    """ Merges two numbers by digit in decreasing order
    >>> merge(31, 42)
    4321
    >>> merge(21, 0)
    21
    >>> merge (21, 31)
    3211
    """
    "*** YOUR CODE HERE ***"
    if n1 ==0:
        return n2
    elif n2 == 0:
        return n1
    elif (n1 % 10) <= (n2 % 10):
        return n1 % 10 + 10 * merge(n1 // 10, n2)
    else:
        return n2 % 10 + 10 * merge(n2 // 10, n1)
