# Implement squareroot function

def square_root(solve_number, guess_root):
    # calculate the guessed number
    guess_number = guess_root * guess_root

    # calculate the difference
    difference = guess_number - solve_number

    # if we are within 1% of target number
    if abs(difference) < (solve_number * 0.01):
        return guess_root
    else:
        return square_root(solve_number, 0.5*(guess_root + solve_number/guess_root))
        
if __name__ == "__main__":
    print "Enter the number for a squre root: "
    number_to_solve = float(raw_input())
    print square_root(number_to_solve, number_to_solve)
    
