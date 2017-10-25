# Find pairs in an integer array whose sum is equal to 10 (bonus: do it in linear time)

input_values = [5,2,3,5,6,2,8]

if __name__ == "__main__":
    for first_value in range(0,len(input_values),1):
        for second_value in range(first_value,len(input_values),1):
            if input_values[first_value] + input_values[second_value] == 10:
                print "\nFirst value: \t" + str(input_values[first_value]) 
                print "Second value: \t" + str(input_values[second_value])
    