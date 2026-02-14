def solve_substrings():
    
    sequence = [2, 3, 7, 2, 1, 0, 5, 2, 3, 1, 8, 4, 8]
    A = 10

    print(f"Input sequence: {sequence}")
    print(f"Target sum A: {A}")
    print("-" * 20)
    print("Found substrings:")

    max_length = 0
    #list to store the current sum of the substring
    
    
    for i in range(len(sequence)):
        current_sum = 0
        for j in range(i, len(sequence)):
            current_sum += sequence[j]
            
            if current_sum == A:
                sub = sequence[i : j + 1]
                # Print output exactly as requested: comma separated
                print(*sub, sep=", ")
                
                if len(sub) > max_length:
                    max_length = len(sub)
            
            # Since we have 0 in the list, we cannot simply break if sum > A
            # We must continue checking.
 #----logic of the task:
# We iterate through the list with two nested loops to find all possible substrings.
# The outer loop starts at each index, and the inner loop extends the substring until the end of the list.
# We keep a running sum of the current substring and check if it equals A.
# If it does, we print the substring and update the maximum length if necessary.

    print("-" * 20)
    print(f"Maximum number of elements: {max_length}")

if __name__ == "__main__":
    solve_substrings()