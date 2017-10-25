# Write a function that prints out the binary form of an int
# Recursive implementation

def binary_form(binary_string, number):
    if number == 0:
        return binary_string
    else:
        if number % 2 == 1:
            binary_string = "1" + binary_string 
        else:
            binary_string = "0" + binary_string
        return binary_form(binary_string, number/2)

if __name__ == "__main__":
    print "Enter decimal number to turn into binary: "
    number = int(raw_input())
    print binary_form("", number)