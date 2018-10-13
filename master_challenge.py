#master challenge
import random

class SecurePrng:
    def __init__(self):
        self.p = 4646704883L
        self.x = random.randint(0, self.p)
        self.y = random.randint(0, self.p)
 
    def next(self):
        self.x = (2 * self.x + 3) % self.p
        self.y = (3 * self.y + 9) % self.p
        return (self.x ^ self.y)

    def get_x(self):
    	return self.x

    def get_y(self):
    	return self.y

def main():
	obj1 = SecurePrng()
	x = obj1.get_x()
	y = obj1.get_y()

	s1 = obj1.next()
	s2 = obj1.next()
	
	
	
	print "--------------------------------"
	print "Result one of PRNG: ", s1
	print "Result two of PRNG: ", s2
	print "--------------------------------"
	print 
	print "-Time for you to give me x and y!-"
	print "Okay so I am gonna give you 5 chances to guess the correct answer!"
	
	
	for i in range(5):	
		
		x1 = raw_input("Give me x: ")
		y1 = raw_input("Give me y: ")

		print 
		print "--------------Results-----------"
		if x1 == x and y1 == y:
			print "Yay! The answer is correct! You are a pro!"
			exit()
		else:
			print "Ah! Sorry! Better luck next time! You have " + str(4-i) + " chances left" 
	print "Oops, it's okay"

if __name__ == '__main__':
        main()

	
	
	
	
