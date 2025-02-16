def recursive_football(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return recursive_football(n-1) + recursive_football(n-2) + recursive_football(n-3) + recursive_football(n-6)
    
print(recursive_football(7))    