def factorial (input_number):
    output_number = 1
    while (input_number > 1):
        output_number *= input_number
        input_number -= 1
    return output_number

if __name__ == "__main__":
    print "Enter a number to compute the factorial of: "
    input_number = int(raw_input())
    print "The factorial is: " + str(factorial(input_number))