# Implement squareroot function

def square_root(test_number, number):
    # calculate the difference
    difference =  test_number * test_number - number

    # if we are within 1% of target number
    if difference < number * 0.01:
        return test_number
    else:
        return ((number-test_number*test_number)/2, number)
        
if __name__ == "__main__":
    print "Enter the number for a squre root: "
    number = float(raw_input())
    print square_root(1.0, number)
    
