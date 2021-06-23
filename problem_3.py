print("Running PROBLEM 3 solutions", end="\n\n")

# SOLUTION 1 -------------------------------------------------------------------

def generateDocument(characters, document):
	for char in document:
		if characters.count(char) < document.count(char):
			return False
	return True

answer = generateDocument(characters="rabcaradabda", document="abracadabra")
print(f"First solution's answer: {answer}")

# SOLUTION 2 -------------------------------------------------------------------

def generateDocument(characters, document):
	alreadyIterated = set()
	for char in document:
		if char not in alreadyIterated:
			if characters.count(char) < document.count(char):
				return False
			alreadyIterated.add(char)
			
	return True

answer = generateDocument(characters="rabcarradabda", document="abracadabra")
print(f"Second solution's answer: {answer}")

# SOLUTION 3 -------------------------------------------------------------------

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

answer = generateDocument(characters="rabcarradabda", document="abracadabra")
print(f"Third solution's answer: {answer}")

