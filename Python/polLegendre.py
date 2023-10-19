import sympy as sp


def polLegendre(n):
    x = sp.Symbol("x")
    p0, p1 = 1, x

    for i in range(2, n+1):
        pk = sp.simplify(((2 * i - 1) * x * p1 - (i - 1) * p0) / i)
        p0 = p1
        p1 = pk

    return p1  


print(polLegendre(2))
