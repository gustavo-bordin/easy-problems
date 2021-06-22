# Problem 1

Write a function that takes in a non-empty array of distinct integers and an
integer representing a target sum. If any two numbers in the input array sum
up to the target sum, the function should return them in an array, in any
order. If no two numbers sum up to the target sum, the function should return
an empty array.

<i>Note that the target sum has to be obtained by summing two different integers
in the array; you can't add a single integer to itself in order to obtain the
target sum.</i>

You can assume that there will be at most one pair of numbers summing up to
the target sum.

<br>

Input example: 
```
array = [1, 5, 3, -10, 20, 13]
targetSum = 18
```

Output example: 
```
[5, 13]
```

<br>

___

<br>



## Solution 1 (Simple and direct):

```python
def twoNumberSum(array, targetSum):
	for number in array:
		for number2 in array:
			if number + number2 == targetSum and number != number2:
				return [number, number2]
		
	return []
```

In the above solution we go through the most simple solution; iterate the array twice, the first time getting a number and the second time verifying if the first number plus the second number is equal to the target sum, returning these two if yes. If there is no matching sum, them it will return an empty array at the end of the loop.

<br>

___

<br>


## Solution 2 (A bit faster):

```python
def twoNumberSum(array, targetSum):
	for n1_index, first_num in enumerate(array):
		for n2_index in range(n1_index + 1, len(array)):
			second_num = array[n2_index]
			if first_num + second_num == targetSum and first_num != second_num:
				return [first_num, second_num]
		
	return []
```

Can you see why it is a bit faster? That's because the loops are not being fully iterated, instead, in the second loop, we are iterating it only after de first index, that's why it is using n1_index + 1. Think, if we already checked the sum of the first_num with all the other numbers, why would i check the sum of the second number with first_num again? It has already been checked.

<br>


___

<br>



## Solution 3 (A cool idea):

```python
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
```

The main idea in the above solution is to sort the array and assign it two pointers, one for the very left value (let's call it L) and another for the very right (let's call it R). As we sorted it, the very left is going to contain the smallest number, and the right one is going to take the biggest. The algorithm is going to sum L with R, if the sum is smaller than the targetSum, so we should walk one step with the left pointer, because if we want a bigger number, we should sum bigger numbers. Let's see a visual example:
 
 ```
   L               R
[-4, -1, 2, 3, 5, 9]

L + R = 5
```
If our target sum is 8, we should walk forward with L, see:

```
      L           R
[-4, -1, 2, 3, 5, 9]

L + R = 8
```
But what if our sum is greater than the targetSum? Let's assume that our targetSum is 1, In this case we just walk backward with the R pointer, see:

```
  L            R
[-4, -1, 2, 3, 5, 9]

L + R = 1
```

<br>

___

<br>


## Solution 4 (An elegant-not-phant one):

```python
def twoNumberSum(array, targetSum):
	map_ = {}

    for number in array:
        potential_match = targetSum - number
        if potential_match in map_:
            return [potential_match, number]
        
        map_[number] = True
    
    return []
```

The above solution may look hard to understand at glance, but it is very simple. We have a map_ which stores every iterated number. The idea is to get the x that the iterated number needs to match the targetSum, this X is the potential_match variable. Look, the diff of targetSum and number is what we want to sum with number to achieve the targetSum. In every iteration we ask to map_ if it has that diff (the number we need to complete the sum), if so, that is the answer, if not, then we save the current iterated on map_, because it may be the lefting number of another iteration.