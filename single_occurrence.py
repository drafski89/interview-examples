# Find the only element in an array that only occurs once.

def single_occurence(list):
    base_pos = 0
    if len(list) == 1:
        return list[base_pos]
    for base_pos in range(len(list)):
        base_value = list[base_pos]
        if base_value is not None:
            for check_pos in range(base_pos+1, len(list)):
                if list[check_pos] is not None and list[check_pos] == base_value:
                    list[check_pos] = None
                    list[base_pos] = None
        if list[base_pos] is not None:
            return base_value

if __name__ == "__main__":
    check_list = [1,1,2,2,3,3,4,5,5]
    print single_occurence(check_list)