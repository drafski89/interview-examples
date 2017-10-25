# Find the common elements of 2 int arrays

a = [1,2,3,4,5,6,7,8,9]
b = [0,1,4,7,9]
results = []

def find_common_elements(a, b):
    for a_pos in range(len(a)):
        a_value = a[a_pos]
        for b_pos in range (len(b)):
            b_value = b[b_pos]
            if a_value == b_value:
                results.append(a_value)

if __name__ == "__main__":
    find_common_elements(a,b)
    print results