# SOLUTION 1 -------------------------------------------------------------------

def isPalindrome(string):
	len_string = len(string) - 1
	len_half_string = len_string // 2
	parts = string.split(string[len_half_string])
	if parts[0] == parts[-1][::-1]:
		return True
	return False

answer = isPalindrome(string="abcdcba")
print(f"First solution's answer: {answer}")

# SOLUTION 2 -------------------------------------------------------------------

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

answer = isPalindrome(string="abcdcba")
print(f"Second solution's answer: {answer}")

# SOLUTION 3 -------------------------------------------------------------------

def isPalindrome(string):
    r_string = string[::-1]

    if string == r_string:
        return True
    return False

answer = isPalindrome(string="abcdcba")
print(f"Third solution's answer: {answer}")

# SOLUTION 4 -------------------------------------------------------------------

def isPalindrome(string, first_char=0):
    last_char = len(string) - 1 - first_char

    if first_char >= last_char:
        return True

    return string[first_char] == string[last_char] and isPalindrome(string, first_char + 1)

answer = isPalindrome(string="abcdcba")
print(f"Third solution's answer: {answer}")
