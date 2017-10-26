# Implement binary search in a rotated array (ex. {5,6,7,8,1,2,3})

array = [5,6,7,8,1,2,3,4]
element = 6

def bin_search(array, element):
    # reorganize the array
    min_value = array[0]
    index = 0
    for position in range(len(array)):
        value = array[position]
        if value < min_value:
            min_value = value
            index = position
    new_array = array[index:] + array[0:index]
    print new_array
    
    # perform the binary search
    return binary_search(new_array, element)
    
def binary_search(array, element):
    # check for length == 0
    if len(array) == 0:
        return False
    
    # split the array in half
    test_element = array[len(array)/2]
    
    # if the element is the test element, return true
    if test_element == element:
        return True
    
    # search upper half or lower half
    if test_element > element:
        return binary_search(array[0:len(array)/2], element)
    else:
        return binary_search(array[len(array)/2+1:], element)
        
if __name__ == "__main__":
    print bin_search(array, element)