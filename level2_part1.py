def solution(num_list, target):
    start_index = 0
    end_index = 1
    tot = num_list[0]

    while True:
        if tot == target:
            return [start_index, end_index - 1]
        elif tot > target:
            # Total too big
            tot -= num_list[start_index] # Update new total
            start_index += 1 # Increment start index
        else:
            # Total too small
            # Check to see if the end index can be increased
            if end_index == len(num_list):
                # No solution
                return [-1, -1]
            tot += num_list[end_index] # Update new total
            end_index += 1 # Increment end index

if __name__ == '__main__':
    print(solution([1, 2, 3, 4], 15)) # Expected: [-1, -1]
    print(solution([4, 3, 10, 2, 8], 12)) # Expected: [2, 3]