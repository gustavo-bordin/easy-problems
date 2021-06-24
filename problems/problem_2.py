# SOLUTION 1 -------------------------------------------------------------------

def firstNonRepeatingCharacter(string):
    for index, char in enumerate(string):
        if string.count(char) == 1:
            return index
        
    return -1

answer = firstNonRepeatingCharacter(string="abracadabra")
print(f"First solution's answer: {answer}")

# SOLUTION 2 -------------------------------------------------------------------

def firstNonRepeatingCharacter(string):
	for index in range(len(string)):
		found_duplicate = False
		
		for index2 in range(len(string)):
			if string[index] == string[index2] and index != index2:
				found_duplicate = True
				
		if not found_duplicate:
			return index
		
	return -1

answer = firstNonRepeatingCharacter(string="abracadabra")
print(f"Second solution's answer: {answer}")

# SOLUTION 3 -------------------------------------------------------------------

def firstNonRepeatingCharacter(string):
	char_frequencies = {}
	
	for character in string:
		char_frequencies[character] = char_frequencies.get(character, 0) + 1
		
	for index in range(len(string)):
		character = string[index]
		if char_frequencies[character] == 1:
			return index
	
	return -1

answer = firstNonRepeatingCharacter(string="abracadabra")
print(f"Third solution's answer: {answer}")

