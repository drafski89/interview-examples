# Implement parseInt
# Implementing casting to an int from a string

if __name__ == "__main__":
    print "Enter a number: "
    str_number = raw_input()[0]
    ascii_value = ord(str_number)
    
    ASCII_ZERO_OFFSET = 48
    
    int_number = ascii_value - ASCII_ZERO_OFFSET
    
    print "This is now an int: " + str(int_number)