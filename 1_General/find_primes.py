# Use dynamic programming to find the first X prime numbers

def find_primes(number):
    current_number = 1
    prime_list = []
    for count in range(number):
        while check_prime(current_number) is False:
            current_number = current_number + 1
        prime_list.append(current_number)
        current_number = current_number + 1
    return prime_list
    
def check_prime(number):
    count = 2
    while count < number/2 + 1:
        if number % count == 0:
            return False
        count = count + 1
    return True
    
if __name__ == "__main__":
    print "Enter the number of primes you'd like: "
    while True:
        number = int(raw_input())
        print find_primes(number)