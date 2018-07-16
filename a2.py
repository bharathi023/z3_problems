from z3 import *

x = Real('x')

s = Solver()
s.add(x ** 2 - 2*x + 1 == 0)
s.check()
print s.model()

