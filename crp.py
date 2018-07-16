from z3 import *

x = Int('x')


s = Solver()

s.add(x%3 == 2)
s.add(x%5 == 3)
s.add(x%7 == 2)

print s.check()
print s.model()

