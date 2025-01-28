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
    
s1 = "senator"
s2 = "treason"

print(anagram_1(s1, s2)) # True