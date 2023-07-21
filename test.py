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


def flatten(s):
    ret = []

    def helper(x, y):
        for i in range(len(x)):
            if type(x[i]) == list:
                return helper(x[i], y)
            else:
                print(x[i])
                y.append(x[i])

    helper(s, ret)
    return ret


x = [1, [2, 3], 4]
print(flatten(x))





def tree(label, branches=[]):
    """Construct a tree with the given label value and a list of branches."""
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [label] + list(branches)


def label(tree):
    """Return the label value of a tree."""
    return tree[0]


def branches(tree):
    """Return the list of branches of the given tree."""
    return tree[1:]


def is_tree(tree):
    """Returns True if the given tree is a tree, and False otherwise."""
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True


def is_leaf(tree):
    """Returns True if the given tree's list of branches is empty, and False
    otherwise.
    """
    return not branches(tree)


def print_tree(t, indent=0):
    """Print a representation of this tree in which each node is
    indented by two spaces times its depth from the root.

    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    """
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)


def copy_tree(t):
    """Returns a copy of t. Only for testing purposes.

    >>> t = tree(5)
    >>> copy = copy_tree(t)
    >>> t = tree(6)
    >>> print_tree(copy)
    5
    """
    return tree(label(t), [copy_tree(b) for b in branches(t)])



def replace_loki_at_leaf(t, lokis_replacement):
    j = 0
    k = []
    for i in branches(t):

        if is_leaf(i):
            if i == 'loki':
                k.append('loki')
            else:
                k.append(i)
        if is_tree(i):
            k.append(replace_loki_at_leaf(i, lokis_replacement))
        j += 1
    return k


yggdrasil = tree('odin',
                 [tree('balder',
                       [tree('loki'),
                        tree('freya')]),
                  tree('frigg',
                       [tree('loki')]),
                  tree('loki',
                       [tree('sif'),
                        tree('loki')]),
                  tree('loki')])





print_tree(replace_loki_at_leaf(yggdrasil, 'freya'))