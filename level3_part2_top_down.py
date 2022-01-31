def count(height, left, memo):
    # Height: the height of the current stair
    # Left: the number of bricks left
    
    # All the bricks have been used, so a full staircase has been made
    if left == 0:
        return 1

    # There are not enough bricks to build a second stair, so an invalid combination
    if left < height:
        return 0

    # Check that the combination has not already been cached
    comb = (height, left)
    if comb in memo:
        # Use the pre-caculated example
        return memo[comb]

    # Get number of combinations for either:
    # - The next stair (so decrease the number of remaining bricks) and increase the minimum height
    # - The same stair, but with an increased minimum height
    numb_combs =  count(height + 1, left - height, memo) + count(height + 1, left, memo)
    # Add value to memo cache
    memo[comb] = numb_combs
    # Return the caculated value
    return numb_combs

def solution(n):
    # Start with a stair of minimum starting height 1 (ascending staricase), with n bricks
    # Minus one as a the single stair combination is not allowed (i.e must be at least 2 stairs)
    
    memo = {}
    return count(1, n, memo) - 1

if __name__ == '__main__':
    for i in range(201):
        print(i, solution(i))