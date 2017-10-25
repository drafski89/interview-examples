# Given 2 integer arrays, determine of the 2nd array is a rotated version of the 1st array. 
# Ex. Original Array A={1,2,3,5,6,7,8} Rotated Array B={5,6,7,8,1,2,3}

a = [1,2,3,4,5,6,7,8]
b = [5,6,7,8,1,2,3,4]

def check_rotated_arrays(a, b):
    # check that the lengths are the same
    if len(a) != len(b):
        return False
    # check find the start point of a inside b
    start_position = 0
    for x in range (0, len(a)):
        if b[x] == a[0]:
            start_position = x
            break
    # check if it is a rotation
    for a_pos in range(0, len(a)):
        b_pos = (start_position + a_pos) % len(a)
        if a[a_pos] != b[b_pos]:
            return False
    return True
    
if __name__ == "__main__":
    print check_rotated_arrays(a, b)