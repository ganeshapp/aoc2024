def read_input():
    left_nums = []
    right_nums = []
    with open('day1/input.txt', 'r') as f:
        for line in f:
            if line.strip():  # Skip empty lines
                nums = line.strip().split()
                left_nums.append(int(nums[0]))
                right_nums.append(int(nums[1]))
    return left_nums, right_nums

def calculate_similarity_score(left_nums, right_nums):
    total_score = 0
    
    # Convert right list to a frequency dictionary
    right_freq = {}
    for num in right_nums:
        right_freq[num] = right_freq.get(num, 0) + 1
    
    # For each number in left list, multiply by its frequency in right list
    for left_num in left_nums:
        frequency = right_freq.get(left_num, 0)  # Get frequency (0 if not found)
        total_score += left_num * frequency
        
    return total_score

# Read input
left_nums, right_nums = read_input()

# Calculate and print result
similarity_score = calculate_similarity_score(left_nums, right_nums)
print(f"Similarity score: {similarity_score}")
