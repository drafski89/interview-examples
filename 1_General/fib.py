def fib_iter(number):
    fib1 = 0
    fib2 = 1
    while number > 0:
        sum = fib1+fib2 
        print "{}".format(sum)
        fib1 = fib2
        fib2 = sum
        number = number-1
        
def fib_rec(fib1, fib2, number):
    if number > 0:
        print "{}".format(fib1+fib2)
        fib_rec(fib2,fib1+fib2,number-1)
        
        
if __name__ == "__main__":
    # no error checking on input
    input_number = raw_input()
    input_number = int(input_number)
    print "Now starting fib iteratively: "
    fib_iter(input_number)
    print "Now starting fib recursively: "
    fib_rec(0,1,input_number)