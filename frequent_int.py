# Find the most frequent integer in an array

# The input array
input_array = [1,2,3,4,5,6,5,2,1,5]
# Answer should be 5

if __name__ == "__main__":
    max_value = max(input_array)
    count_array = [0 for x in range(max_value+1)]
    for value in input_array:
        count_array[value] = count_array[value] + 1
    max_count  = max(count_array)

    for position in range(len(count_array)):
        if max_count == count_array[position]:
            print "Max occurence value is: " + str(max_count) + "."
            print "Occurs with value: " + str(position)
    