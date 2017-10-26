# Write a multiply function that multiples 2 integers without using *

def add_multiply(base, multiply):
	if multiply <= 1:
		return base
	return base + add_multiply(base, multiply-1)
	
if __name__ == "__main__":
	print "Enter the number for a base: "
	base = int(raw_input())
	print "Enter the number for a multiply: "
	multiply = int(raw_input())
	print add_multiply(base, multiply)