def cascade(n):
    if n < 10:
        print(n)
    else:
        print(n)
        cascade(n // 10)
        print(n)


cascade(124568)


def cascade1(n):
    print(n)
    if n >= 10:
        cascade1(n // 10)
        print(n)


cascade1(59651641)


def inverse_cascade(n):
    grow(n)
    print(n)
    shrink(n)


def f_then_g(f, g, n):
    if n:
        f(n)
        g(n)


grow = lambda n: f_then_g(grow, print, n // 10)
shrink = lambda n: f_then_g(print, shrink, n // 10)


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 2) + fib(n - 1)


def pingpong(n):
    def check_contain(x):
        if x < 8 or 8 < x < 10:
            return False
        elif x % 10 == 8:
            return True
        else:
            return check_contain(x // 10)

    def helper(x):
        if x == 1:
            return 1
        if x % 8 == 0 or check_contain(x):
            return -helper(x - 1)
        else:
            return helper(x - 1)

    if n == 1:
        return 1
    if n > 1:
        return pingpong(n - 1) + helper(n - 1)


print(pingpong(100))

"""
    i = 1
    j = 0
    k = 1

    while i <= n:
        if i % 8 == 0 or check_contain(i):
            j = j + k
            k = k * -1
            print(i, j)
        else:
            j = j + k
            print(i, j)
        i += 1
    return j
"""
"""Typing test implementation"""




