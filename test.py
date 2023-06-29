def square(x):
    return x * x

def successor(k):
    return k + 1

def compose1(f, g):
        def h(x):
            return f(g(x))
        return h
add_one_and_square = compose1(square, successor)
print(add_one_and_square(12))
