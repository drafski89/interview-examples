# Given a function rand5() that returns a random int between 0 and 5, implement rand7()

import random

def rand5():
	return random.randrange(0,5)

if __name__ == "__main__":
	print int(7*(rand5()/5.0))