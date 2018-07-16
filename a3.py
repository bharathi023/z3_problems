from z3 import *


x,y =Ints('x y')

t = Solver()
t.add(And((x+y == -3),(x*y == 2)))
print t.check()
print t.model()


