# Implement an exponent function (bonus: now try in log(n) time)

def exp(base, power):
	if power <= 1:
		return base
	return base * exp(base, power - 1)

if __name__ == "__main__":
	print "Enter the number for a base: "
	base = int(raw_input())
	print "Enter the number for a exponential: "
	exponential = int(raw_input())
	print exp(base, exponential)