def solution(xs):

    # Check if xs contains zero
    contain_zero = False
    if 0 in xs:
        contain_zero = True

    # Collect positive ints, ignoring 0
    pos = [num for num in xs if num > 0]

    # Collect negative ints, ignoring 0
    neg = [num for num in xs if num < 0]

    # If length of negative nums is odd, remove the smallest value (closest to zero)
    if len(neg) % 2:
        removed = max(neg)
        neg.remove(removed)

    # Combine
    nums = neg + pos

    # Return no elements returned, return 0 if there was a zero, otherwise return string of the greatest negative number
    if not len(nums):
        if contain_zero:
            return '0'
        else:
            return str(removed)

    # Get product of both negative and positive numbers
    product = 1
    for val in nums:
        product *= val
    
    return str(product)

if __name__ == '__main__':
    print(solution([-6]))
    print(solution([-2, -3, 4, -5]))
    print(solution([0, 0, -0]))
    print(solution([2, -3, 1, 0, -5]))
    print(solution([-1, -1, -1, -1, -1]))