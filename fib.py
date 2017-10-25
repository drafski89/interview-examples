def fib_iter(number):
    fib1 = 0
    fib2 = 1
    while number > 0:
        sum = fib1+fib2 
        print "{}".format(sum)
        fib1 = fib2
        fib2 = sum
        number = number-1
        
        
if __name__ == "__main__":
    # no error checking on input
    input_number = raw_input()
    input_number = int(input_number)
    print "Now starting fib iteratively: "
    fib_iter(input_number)