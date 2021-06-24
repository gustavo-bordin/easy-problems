# Summary
- [Problem 1](#p1)
  - [Solution 1](#p1s1)
  - [Solution 2](#p1s2)
  - [Solution 3](#p1s3)
- [Problem 2](#p2)
  - [Solution 1](#p2s1)
  - [Solution 2](#p2s2)
  - [Solution 3](#p2s3)
- [Problem 3](#p3)
  - [Solution 1](#p3s1)
  - [Solution 2](#p3s2)
  - [Solution 3](#p3s3)
- [Problem 4](#p4)
  - [Solution 1](#p4s1)
  - [Solution 2](#p4s2)
  - [Solution 3](#p4s3)
  - [Solution 4](#p4s4)
- [Problem 5](#p5)
  - [Solution 1](#p5s1)
  - [Solution 2](#p5s2)
  
<br>
<br>
<br>
<br>
<br>

<div id="p1">

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
</div>

<br>

___

<br>


<div id="p1s1">

#### Solution 1 (Simple and direct):

```python
def twoNumberSum(array, targetSum):
	for number in array:
		for number2 in array:
			if number + number2 == targetSum and number != number2:
				return [number, number2]
		
	return []
```

In the above solution we go through the most simple solution; iterate the array twice, the first time getting a number and the second time verifying if the first number plus the second number is equal to the target sum, returning these two if yes. If there is no matching sum, them it will return an empty array at the end of the loop.
</div>

<br>

___

<br>

<div id="p1s2">

#### Solution 2 (A bit faster): <a name="p2"></a>

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
</div>
<br>


___

<br>


<div id="p1s3">

#### Solution 3 (A cool idea):

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
</div>
<br>

___

<br>

<div id="p1s4s">

### Solution 4 (An elegant-not-phant one):

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
</div>

<br>
<br>
<br>

___

<br>
<br>
<br>

<div id="p2">

# Problem 2


Write a function that takes in a string of lowercase English-alphabet letters
and returns the index of the string's first non-repeating character.

The first non-repeating character is the first character in a string that
occurs only once.

If the input string doesn't have any non-repeating characters, your function
should return -1

<br>

Input example: 
```
string = "abracadabra"
```

Output example: 
```
4 // Because the first non-repeating character is C, which is in index 4
```
</div>

<br>


___

<br>

<div id="p2s1">

### Solution 1 (Adorable):

```python
def firstNonRepeatingCharacter(string):
    for index, char in enumerate(string):
		if string.count(char) == 1:
			return index
		
	return -1
```

You may already got it, it is sooo simple. In order to find the first non-repeating number, whe just iterate through each character in the string counting the times it appears in the main string. If the iterated character appears once, then it is the right one.
</div>
<br>


___

<br>

<div id="p2s2">

### Solution 2 (I'm deciding if i like it):

```python
def firstNonRepeatingCharacter(string):
	for index in range(len(string)):
		found_duplicate = False
		
		for index2 in range(len(string)):
			if string[index] == string[index2] and index != index2:
				found_duplicate = True
				
		if not found_duplicate:
			return index
		
	return -1
```

In this solution we the main string twice, the idea is to find a character and then iterate again verifying if this character appears more in the string. If yes, we se found_duplicate to true, which triggers the first loop again, making it iterate the next character. Once it does not found the same character two times, found_duplicate will be False, making it return the index. If there is no non-repeating character, then it return -1 at the end of the loops.
</div>

<br>


___

<br>

<div id="p2s3">

### Solution 3 (ª.ª):

```python
def firstNonRepeatingCharacter(string):
	char_frequencies = {}
	
	for character in string:
		char_frequencies[character] = char_frequencies.get(character, 0) + 1
		
	for index in range(len(string)):
		character = string[index]
		if char_frequencies[character] == 1:
			return index
	
	return -1
```

This one is simple too, it creates a hash map with all the characters of the string. This hash map is going to get the character as key and the times this character appears in the string as value. Then after inserting all the characters, it iterates the string again checking if the iterated character appears only once, if yes then returns its index, if not, return -1 at the end of the loops.
</div>
<br>
<br>
<br>

___

<br>
<br>
<br>

<div id="p3">

# Problem 3

You're given a string of available characters and a string representing a
document that you need to generate. Write a function that determines if you
can generate the document using the available characters. If you can generate
the document, your function should return true, otherwise it should return false

You're only able to generate the document if the frequency of unique
characters in the characters string is greater than or equal to the frequency
of unique characters in the document string. For example, if you're given characters = "abcabc" and document = "aabbccc" you cannot generate the document because you're missing one `c`

The document that you need to create may contain any characters, including
special characters, capital letters, numbers, and spaces.

<br>

Input example: 
```
characters = "da ab e r xis aca de bra"
document = "abracadabra"
```

Output example: 
```
True
```
</div>

<br>


___

<br>

<div id="p3s1">

### Solution 1 (A very simple one):

```python
def generateDocument(characters, document):
	for char in document:
		if characters.count(char) < document.count(char):
			return False
	return True
```

It iterates the characters counting if the iterated one appears less in characters than it appears in document. If so, then the result if false, because we are not able to generate the document if we don't have all the characters. After the loop it returns True, because if there is no lefting character in characters string, then we have everything we need to generate.
</div>
<br>

___

<br>

<div id="p3s2">

### Solution 2 (A very simple one faster edition)

```python
def generateDocument(characters, document):
	alreadyIterated = set()
	for char in document:
		if char not in alreadyIterated:
			if characters.count(char) < document.count(char):
				return False
			alreadyIterated.add(char)
			
	return True
```

It is the same as solution 1, but it adds the iterated char in a set in order to do not iterate the same char multiple times, it saves time, that's why it is faster :-)
</div>
<br>

___

<br>
<div id="p3s3">

### Solution 3 (The famous hash map):

```python
def generateDocument(characters, document):
	character_counts = {}
	
	for character in characters:
		if character not in character_counts:
			character_counts[character] = 0
		
		character_counts[character] += 1
	
	for character in document:
		if character not in character_counts or character_counts[character] == 0:
			return False
		
		character_counts[character] -= 1
		
	return True
```

In the above solution it is created a hash map with the counts of each character. The first for loop created this count. Then, it checks each character in the document string, verifying if the iterated character does not exists in the map or its count is 0 (it exists but there is no enough occurrences to generate the document).
</div>
<br>
<br>
<br>

___

<br>
<br>
<br>

<div id="p4">

# Problem 4


Write a function that takes in a non-empty string and that returns a boolean
representing whether the string is a palindrome.

A palindrome is defined as a string that's written the same forward and
backward. Note that single-character strings are palindromes.

<br>

Input example: 
```
string = "abcdcba"
```

Output example: 
```
True
```
</div>

<br>


___

<br>

<div id="p4s1">

### Solution 1 (Nice way):

```python
def isPalindrome(string):
	len_string = len(string) - 1
	len_half_string = len_string // 2
	parts = string.split(string[len_half_string])
	if parts[0] == parts[-1][::-1]:
		return True
	return False
```

It splits the string in the middle, getting the left and the right part. Then it checks if the first part is equal to the reverse of the second part, see:

```
raw string = abcdbca

           L         R
splited = [abc, d, cba]

if L == the reverse of R (abc)? Yes
```
</div>


<br>


___

<br>
<div id="p4s2">

### Solution 2

```python
def isPalindrome(string):
    l = 0
	r = -1
	
	len_half_str = len(string) // 2
	
	while l < len_half_str:
		l_char = string[l]
		r_char = string[r]
		
		if l_char != r_char:
			return False
		
		l += 1
		r -= 1
		
	return True
```

In this solution we assign to pointers, one to the left part and another to the right part, then while the left pointer in less than the len of half of the string, we check if the left pointer and the right pointer are different, if yes, we return False because if they are different, the string is not a palindrome. After this check we move the left pointer forward and the right pointer backward to keep track of the other characters. After checking all the characters, if none of them are different, then we return True. See a visual example:

```
L           R
a b c d c b a

L == R? Yes.

  L       R
a b c d c b a

L == R? Yes. Then keep on doing this until check every character.
```
</div>
<br>


___

<br>
<div id="p4s3">

### Solution 3 (The best one)

```python
def isPalindrome(string):
    r_string = string[::-1]
	
	if string == r_string:
		return True
	return False
```

Just reverse the string and check if the reversed is equal the normal, thats what we do in our mind when we see a palindrome word :) Quick and easy.
</div>
<br>


___

<br>
<div id="p4s4">

### Solution 4 (A recursive mode)

```python
def isPalindrome(string, first_char=0):
    last_char = len(string) - 1 - first_char
	
	if first_char >= last_char:
		return True

	return string[first_char] == string[last_char] and isPalindrome(string, first_char + 1)
```

First it set two pointers, one for the first character and another for the last, then it checks if every character were checked, returning True if yes. Otherwise, it returns a boolean condition checking if both pointers are equal and calling itself again. If both pointers are different, then it will return False.
</div>

<br>
<br>
<br>

___

<br>
<br>
<br>

<div id="p5">

# Problem 5

There's an algorithms tournament taking place in which teams of programmers
compete against each other to solve algorithmic problems as fast as possible.
Teams compete in a round robin, where each team faces off against all other
teams. Only two teams compete against each other at a time, and for each
competition, one team is designated the home team, while the other team is the
away team. In each competition there's always one winner and one loser; there
are no ties. A team receives 3 points if it wins and 0 points if it loses. The
winner of the tournament is the team that receives the most amount of points.


Given an array of pairs representing the teams that have competed against each
other and an array containing the results of each competition, write a
function that returns the winner of the tournament. The input arrays are named competitions and results, respectively. The competitions array has elements in the form of [homeTeam, awayTeam], where each team is a string of at most 30 characters representing the name of the team. The results  array contains information about the winner of each corresponding competition in the competitions array. Specifically, results[i] denotes the winner of competitions[i], where a 1 in the results  array means that the home team in the corresponding competition won and a 0  means that the away team won.
<br>

Input example: 
```json
competitions = [
  ["HTML", "C#"],
  ["C#", "Python"],
  ["Python", "HTML"],
]

results = [0, 0, 1]
```

Output example: 
```
Python 
// Because C# beats HTML, Python beats C# and Python beats HTML
// Python - 6
// C#     - 3
// HTML   - 0
```
</div>

<br>


___

<br>

<div id="p5s1">

### Solution 1 (Simple and ugly):

```python
def tournamentWinner(competitions, results):
	map_ = {}
	
	for index, team in enumerate(competitions):
		winner = team[1 if results[index] == 0 else 0]
		
		if winner not in map_:
			map_[winner] = 0
			
		map_[winner] += 3
	
	highest_value = -1
	highest_name = 0
	for k,v in map_.items():
		if v > highest_value:
			highest_value = v
			highest_name = k
	
	return highest_name
```

We create a map that is going to contain the team name as key and the team score as value. The competitions list is iterated getting the winner team of that round (If the element of the same index in results is 0, then the second team won, otherwise the victory is of the first team). Then it is created that winner team in the map if it is not created yet, and then added the points to it. After every team was iterated, we count the highest score and return the team that did it.
</div>

<br>


___

<br>

<div id="p5s2">

### Solution 2 (Beautiful, clean and readable)

```python
def tournamentWinner(competitions, results):
	map_ = {'winning': {'score': 0, 'name': None}}
	
	def add_points(winner):
		if winner not in map_:
			map_[winner] = 0
		
		map_[winner] += 3
		
	def update_best_team(winner):
		if map_[winner] > map_['winning']['score']:
			map_['winning']['score'] = map_[winner]
			map_['winning']['name'] = winner
	
	for index, team in enumerate(competitions):
		winner = team[1 if results[index] == 0 else 0]
		add_points(winner)
		update_best_team(winner)
		
	return map_['winning']['name']
```

It is the same solution as above, but instead of iterating the map getting the highest score, we have a key named winning, and we assign the team which has the highest score on every iteration. It also was rewrote in order to be readable, following the best practices.
</div>