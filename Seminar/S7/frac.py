from math import gcd


class Frac:
    def __init__(self, n, m):
        self.n = n
        self.m = m

    def extend(self, k):
        self.n *= k
        self.m *= k

    def reduce(self):
        g = gcd(self.n, self.m)
        self.n //= g
        self.m //= g



