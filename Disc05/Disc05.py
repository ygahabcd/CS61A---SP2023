"""
Q1: Tree Abstraction Barrier
Consider a tree t constructed by calling tree(1, [tree(2), tree(4)]). For each of the following expressions, answer
these two questions:
"""


def tree(label, branches=[]):
    """Construct a tree with the given label value and a list of branches."""
    return [label] + list(branches)


def label(tree):
    """Return the label value of a tree."""
    return tree[0]


def branches(tree):
    """Return the list of branches of the given tree."""
    return tree[1:]


def is_leaf(tree):
    """Returns True if the given tree's list of branches is empty, and False
    otherwise.
    """
    return not branches(tree)


t = tree(1, [tree(2), tree(4)])  # [1, [2], [4]]

# 1
label(t)  # 1
# 2
t[0]  # 1
# 3
label(branches(t)[0])  # 2
# 4
is_leaf(t[1:][1])  # True
# 5
[label(b) for b in branches(t)]  # [2, 4]
# 5
branches(tree(5, [t, tree(3)]))[0][0]  # 1


def height(t):
    """Return the height of a tree.

    >>> t = tree(3, [tree(5, [tree(1)]), tree(2)])       # [3, [5, [1]], [2]]
    >>> height(t)
    2
    >>> t = tree(3, [tree(1), tree(2, [tree(5, [tree(6)]), tree(1)])])    #[3, [1], [2, [5, [6]], [1]]]
    >>> height(t)
    3
    """
    if is_leaf(t):
        return 0
    else:
        max_height = 0
        for i in branches(t):
            max_height = max(max_height, height(i))
    return 1 + max_height


def max_path_sum(t):
    """Return the maximum path sum of the tree.

    >>> t = tree(1, [tree(5, [tree(1), tree(3)]), tree(10)])      #[1, [5, [1], [3]], [10]]
    >>> max_path_sum(t)
    11
    """
    if is_leaf(t):
        return t[0]
    else:
        max_sum = 0
        for i in branches(t):
            max_sum = max(max_sum, max_path_sum(i))
    return t[0] + max_sum


def find_path(t, x):
    """
    >>> t = tree(2, [tree(7, [tree(3), tree(6, [tree(5), tree(11)])] ), tree(15)])
    >>> find_path(t, 5)
    [2, 7, 6, 5]
    >>> find_path(t, 10)  # returns None
    """
    if label(t) == x:
        return [x]
    for i in branches(t):
        path = find_path(i, x)
        if type(path) == list:
            return [t[0]] + path


def sum_tree(t):
    """
    Add all elements in a tree.
    >>> t = tree(4, [tree(2, [tree(3)]), tree(6)])
    >>> sum_tree(t)
    15
    """
    if is_leaf(t):
        return t[0]
    else:
        total = 0
        for i in branches(t):
            total += sum_tree(i)
    return t[0] + total


def balanced(t):
    """
    Checks if each branch has same sum of all elements and
    if each branch is balanced.
    >>> t = tree(1, [tree(3), tree(1, [tree(2)]), tree(1, [tree(1), tree(1)])]) #[1, [3], [1, [2]], [1, [1], [1]]]
    >>> balanced(t)
    True
    >>> t = tree(1, [t, tree(1)])
    >>> balanced(t)
    False
    >>> t = tree(1, [tree(4), tree(1, [tree(2), tree(1)]), tree(1, [tree(3)])]) #[1, [4], [1, [2], [1]], [1, [3]]]
    >>> balanced(t)
    False
    """
    "*** YOUR CODE HERE ***"
    if is_leaf(t):
        return True
    else:
        for i in branches(t):
            if sum_tree(branches(t)[0]) != sum_tree(i) or not balanced(i):
                return False
        return True


def sprout_leaves(t, leaves):
    """Sprout new leaves containing the data in leaves at each leaf in
    the original tree t and return the resulting tree.

    >>> t1 = tree(1, [tree(2), tree(3)])
    >>> print_tree1(t1)
    1
      2
      3
    >>> new1 = sprout_leaves(t1, [4, 5])
    >>> print_tree1(new1)
    1
      2
        4
        5
      3
        4
        5

    >>> t2 = tree(1, [tree(2, [tree(3)])])
    >>> print_tree1(t2)
    1
      2
        3
    >>> new2 = sprout_leaves(t2, [6, 1, 2])
    >>> print_tree1(new2)
    1
      2
        3
          6
          1
          2
    """
    if is_leaf(t):
        return tree(t[0], [tree(x) for x in leaves])
    else:
        new_branches = [sprout_leaves(x,leaves) for x in branches(t)]
    return tree(t[0], new_branches)


def print_tree1(t):
    def helper(i, t):
        print("  " * i + str(label(t)))
        for b in branches(t):
            helper(i + 1, b)
    helper(0, t)


def hailstone_tree(n, h):
    """Generates a tree of hailstone numbers that will reach N, with height H.
    >>> print_tree(hailstone_tree(1, 0))
    1
    >>> print_tree(hailstone_tree(1, 4))
    1
        2
            4
                8
                    16
    >>> print_tree(hailstone_tree(8, 3))
    8
        16
            32
                64
            5
                10
    """
    if h <= 0:
        return tree(n)
    branches = [hailstone_tree(n*2, h-1)]
    if (n-1)%3 == 0 and (n-1)/3%2 ==1 and (n-1)/3 > 1:
        branches += [hailstone_tree((n-1)//3, h-1)]
    return tree(n, branches)


def print_tree(t):
    def helper(i, t):
        print("    " * i + str(label(t)))
        for b in branches(t):
            helper(i + 1, b)

    helper(0, t)
