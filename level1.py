def solution(seq):
    """Return max number of equal parts a 'circular' string can be completely split into"""

    # For every possible length of string
    for str_len in range(1, len(seq) + 1):

        # Skip if length is not divisible
        if len(seq) % str_len:
            continue

        # String including the 'wrap around' to generate all possible linear combinations
        comb_seq = seq + seq[:str_len - 1]
        
        # All linear combinations
        combs = set()
        for start_index in range(len(seq)):
            combs.add(comb_seq[start_index:start_index + str_len])

        # For every combination, get the number of times it occurs
        for comb in combs:
            count = comb_seq.count(comb)

            # If the occurance times the length of the string is the length of the original sequence, it fits exactly
            if str_len * count == len(seq):
                
                # Return maximum number of slices
                return count

if __name__ == '__main__':
    print(solution('abcabcabcabc')) # Expected: 4
    print(solution('abccbaabccba')) # Expected: 2