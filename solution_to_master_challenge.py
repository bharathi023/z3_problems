from z3 import *

s1 = input()
s2 = input()
s = Solver()

x,y =BitVecs('x y',35)

s.add( ((2 * x + 3) % 4646704883L) ^ ((3 * y + 9) % 4646704883L) == s1)
s.add( ((2 * ((2 * x + 3) % 4646704883L) + 3) % 4646704883L) ^ ((3 * ((3 * y + 9) % 4646704883L) + 9) % 4646704883L) == s2)                                          
s.add(x<4646704883L)
s.add(x > 0)
s.add(y<4646704883L)
s.add(y > 0)

print s.check()
if(s.check() == sat):
	m = s.model()
	print m[x]
	print m[y]
	s.add(Or(x!=m[x], y!=m[y]))
	
