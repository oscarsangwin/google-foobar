def num_end_zeros(bin_str):
    """Return number of zeros at the end of a string"""
    zeros = 0
    for char in bin_str[::-1]:
        if char == '0':
            zeros += 1
        else:
            break
    return zeros

def solution(n):
    n = bin(int(n))[2:] # Convert from integer to binary string
    steps = 0 # The minimum number of operations it takes to get to 0
    while n != '1':

        if n == '11':
            # Exception - if n is 3, subtract 1, resulting in 2:
            n = '10'

        elif n[-1] == '0':
            # n is even (ends in 0 in binary)

            # Divide by 2 (remove the last character)
            n = n[:-1]
        else:
            # n is odd (ends in 1 in binary)

            # Binary string if 1 is added and if subtracted
            add_str = bin(int(n, 2) + 1)[2:]
            sub_str = bin(int(n, 2) - 1)[2:]

            # Get number of zeros at the end of each string
            add_zeros = num_end_zeros(add_str)
            sub_zeros = num_end_zeros(sub_str)

            if sub_zeros >= add_zeros:
                # Subtract 1
                n = sub_str
            else:
                # Add 1
                n = add_str
        steps += 1

    return steps

if __name__ == '__main__':
    print(solution(4)) # Expected 2
    print(solution(15)) # Expected 5