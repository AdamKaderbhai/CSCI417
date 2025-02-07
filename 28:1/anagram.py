
# Solution 1 : Using dictionaries and frequency counters
def anagram_1(s1, s2):
    frequency_1 = {}
    frequency_2 = {}
    if len(s1) != len(s2):
        return False

    for char in s1:
        if char in frequency_1:
            frequency_1[char] += 1
        else:
            frequency_1[char] = 1

    for char in s2:
        if char in frequency_2:
            frequency_2[char] += 1
        else:
            frequency_2[char] = 1

#compare the two dictionaries

    for char in frequency_1:
        if char not in frequency_2:
            return False
        else:
            if frequency_1[char] != frequency_2[char]:
                return False
    return True
    
s1 = "Ginger"
s2 = "treason"

print(anagram_1(s1, s2)) # True
'''

'''
# Solution 2: Iterate and check off
def anagram_2(s1, s2):
    if len(s1) != len(s2):
        return False

    s1 = list(s1)
    s2 = list(s2)

    for char in s1:
        if char in s2:
            s2.remove(char)
        else:
            return False
    return True
print(anagram_2("ate", "tea")) # True

# Solution 3: Sort and compare
def anagram_3(s1, s2):
    return sorted(s1) == sorted(s2)
'''




'''
def is_perfect_square(n):
    if n < 0:
        return False
    for i in range(n + 1):
        if i * i == n:
            return True
    return False

print(is_perfect_square(16))  # True
print(is_perfect_square(14))  # False
print(is_perfect_square(25))  # True
print(is_perfect_square(26))  # False


