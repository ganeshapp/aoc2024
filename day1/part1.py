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

def calculate_total_distance(left_nums, right_nums):
    # Sort both lists
    left_nums = sorted(left_nums)
    right_nums = sorted(right_nums)
    
    total_distance = 0
    # Calculate distance between corresponding numbers after sorting
    for left, right in zip(left_nums, right_nums):
        distance = abs(left - right)
        total_distance += distance
        
    return total_distance

# Read input
left_nums, right_nums = read_input()

# Calculate and print result
total_distance = calculate_total_distance(left_nums, right_nums)
print(f"Total distance: {total_distance}")
