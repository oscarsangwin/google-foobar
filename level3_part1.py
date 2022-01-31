def solution(nums):
    """Return number of unique lucky tripples posible"""

    # For every num in nums, contains a set which have indexes of factors with a greater index
    nums_factors = []

    for num_index, num in enumerate(nums):
        # Create empty set for next number
        nums_factors.append(set())

        # Every item after the current index
        possible_factors = nums[num_index + 1:]

        # For every item, check if it can divide the current number with no remainder
        for factor_index, factor in enumerate(possible_factors):
            if not factor % num:

                # Add the factor's index to the set
                nums_factors[num_index].add(factor_index + num_index + 1)

    # Count up total number of combinations
    count = 0
    # For every starting num in the factors
    for part1 in nums_factors:
        # For every index in the starting num
        for part2_index in part1:
            # Increment count by the number of possible 3rd parts
            count += len(nums_factors[part2_index])

    return count

if __name__ == '__main__':
    print(solution([1, 2, 3, 4, 5, 6])) # Expected 3
    print(solution([1, 1, 1])) # Expected 1