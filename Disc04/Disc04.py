def count_stair_ways(n):
    """Returns the number of ways to climb up a flight of
    n stairs, moving either 1 step or 2 steps at a time.
    >>> count_stair_ways(4)
    5
    """
    "*** YOUR CODE HERE ***"
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n <= 0:
        return 0
    else:
        return count_stair_ways(n - 1) + count_stair_ways(n - 2)


def count_k(n, k):
    """ Counts the number of paths up a flight of n stairs
    when taking up to and including k steps at a time.
    >>> count_k(3, 3) # 3, 2 + 1, 1 + 2, 1 + 1 + 1
    4
    >>> count_k(4, 4)
    8
    >>> count_k(10, 3)
    274
    >>> count_k(300, 1) # Only one step at a time
    1
    >>> count_k(4, 2)
    5
    >>> count_k(2, 2)
    2
    """
    "*** YOUR CODE HERE ***"
    if n == 0:
        return 1
    elif n < 0:
        return 0
    else:
        i = 1
        total = 0
        while i <= k:
            total += count_k(n - i, k)
            i += 1
        return total


def even_weighted_loop(s):
    """
    Write a function that takes a list s and returns a new list that keeps only the even-indexed elements of s and
    multiplies them by their corresponding index. First approach this problem with a normal for loop (without list
    comprehension).
    >>> x = [1, 2, 3, 4, 5, 6]
    >>> even_weighted_loop(x)
    [0, 6, 20]
    """
    "*** YOUR CODE HERE ***"
    a = []
    for i in s:
        if s.index(i) % 2 == 0:
            a.append(i * s.index(i))
    return a

def even_weighted_comprehension(s):
    """
    Now that you’ve done it with a for loop, try it with a list comprehension
    >>> x = [1, 2, 3, 4, 5, 6]
    >>> even_weighted_comprehension(x)
    [0, 6, 20]
    """
    return [x * (s.index(x)) for x in s if s.index(x) % 2 ==0]
# return [s[i] * i for i in range(0,len(s)) if i % 2 == 0]

def max_product(s):
    """Return the maximum product that can be formed using
    non-consecutive elements of s.
    Write a function that takes in a list and returns the maximum product that can be formed using nonconsecutive
    elements of the list. The input list will contain only numbers greater than or equal to 1.
    >>> max_product([10,3,1,9,2]) # 10 * 9
    90
    >>> max_product([5,10,5,10,5]) # 5 * 5 * 5
    125
    >>> max_product([])
    1
    """
    if s == []:
        return 1
    else:
        with_first = s[0] * max_product(s[2:])
        without_first = max_product(s[1:])
        return max(with_first,without_first)