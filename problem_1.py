print("Running PROBLEM 1 solutions", end="\n\n")

# SOLUTION 1 -------------------------------------------------------------------

def twoNumberSum(array, targetSum):
	for number in array:
		for number2 in array:
			if number + number2 == targetSum and number != number2:
				return [number, number2]
		
	return []

answer = twoNumberSum(array=[-1, 3, -5, 2, 10, 13], targetSum=5)
print(f"First solution's answer: {answer}")

# SOLUTION 2 -------------------------------------------------------------------

def twoNumberSum(array, targetSum):
	for n1_index, first_num in enumerate(array):
		for n2_index in range(n1_index + 1, len(array)):
			second_num = array[n2_index]
			if first_num + second_num == targetSum and first_num != second_num:
				return [first_num, second_num]
		
	return []

answer = twoNumberSum(array=[-1, 3, -5, 2, 10, 13], targetSum=5)
print(f"Second solution's answer: {answer}")

# SOLUTION 3 -------------------------------------------------------------------

def twoNumberSum(array, targetSum):
	array.sort()
	left = 0
	right = len(array) - 1
	
	while left < right:
		sum_ = array[left] + array[right]
		if sum_ == targetSum:
			return [array[left], array[right]]
		elif sum_ < targetSum:
			left += 1
		elif sum_ > targetSum:
			right -= 1
			
	return []

answer = twoNumberSum(array=[-1, 3, -5, 2, 10, 13], targetSum=5)
print(f"Third solution's answer: {answer}")

# SOLUTION 4 -------------------------------------------------------------------

def twoNumberSum(array, targetSum):
    map_ = {}

    for number in array:
        potential_match = targetSum - number
        if potential_match in map_:
            return [potential_match, number]
        
        map_[number] = True

    return []

answer = twoNumberSum(array=[-1, 3, -5, 2, 10, 13], targetSum=5)
print(f"Fourth solution's answer: {answer}")
