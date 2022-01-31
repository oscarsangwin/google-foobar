def solution(n):
    # Print the current combination table (for debugging)
    def show(): [print(row) for row in combs]

    # The possible combinations:
    # - Each row represents the maximum height for a staircase
    # - Each column represents number of bricks to use in that staircase
    combs = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    # Base case - when we have 0 maximum height and 0 bricks, there is only one possible combination
    combs[0][0] = 1

    # For every maximum height (excluding the first row)
    for max_height in range(1, n + 1):

        # For every number of bricks to make the staircase
        for num_bricks in range(n + 1):

            # Set the value to the number of combs in the row above (i.e with the same number of bricks to use, but one less maximum height)
            combs[max_height][num_bricks] = combs[max_height - 1][num_bricks]

            # If the number of bricks is greater than or equal to the maximum bricks for the staircase
            if num_bricks >= max_height:

                # Increase the existing combs by the number of combs when the 1st step is max height
                # (i.e the next step height is max_height - 1 and the number of bricks to use is the left over number after the next step, num_bricks - max_height) 
                combs[max_height][num_bricks] += combs[max_height - 1][num_bricks - max_height]

    # Return the number of combinations when the max height and bricks to use is n, the number of bricks given
    # Minus 1, as the combination of a vertical staircase is not allowed (i.e must be at least 2 steps)
    return combs[n][n] - 1

if __name__ == '__main__':
    print(solution(200))