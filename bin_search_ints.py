# Implement binary search of a sorted array of integers

# Implemented recursively

array = [1,2,3,4,5,6,7,8]
element = 9

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
    print binary_search(array, element)
    