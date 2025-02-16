# given n = ak, ak-1, ..., a1, a0, where 0 <= ai <= 9, 0 <= i <= k,
# write a recursive function that performs binary conversion of n'''
"""
def recursive_binary(n):
    if n == 0:
        return ''
    else:
        return recursive_binary(n // 2) + str(n % 2)
    
#test case
test_case = 2
print(recursive_binary(test_case)) 
"""

"""
# write a Iterative function that performs binary conversion of n
def iterative_binary(n):
    binary = ''
    while n > 0:
        binary = str(n % 2) + binary
        n = n // 2
    return binary
#test case
test_case = 100
print(iterative_binary(test_case)) 

"""

"""
# use for loop to find the sum of all the elements in a list
def sum_list(lst):
    sum = 0
    for i in lst:
        sum += i
    return sum
"""

'''
def nr_binary(n):
    solution = ["" for i in range(0, n+1)]
    solution[0], solution[1] = str(0), str(1)
    m = 2 

    while m <= n:
        solution[m] = solution[m//2] + str(m % 2)
        m += 1
    return solution[n]

print(nr_binary(7))

'''

# Given a total score n in basketball, write a recursive function that returns the number of ways to score n points
'''
def recursive_basketball(n):
    if n == 0:
        return 1
    if n < 0:
        return 0
    return recursive_basketball(n - 1) + recursive_basketball(n - 2) + recursive_basketball(n - 3)

print(recursive_basketball(5)) # 13
'''

'''
def nr_basketball(n):
    pass 

    solution = [0 for i in range(0, n+1)]
    solution[0] = 1
    solution[1] = 1
    solution[2] = 2

    for i in range(3, n+1):
        solution[i] = solution[i-1] + solution[i-2] + solution[i-3]
    return solution[n]

print(nr_basketball(6)) # 13

# big O notation for recursive function is O(3^n) and for iterative function is O(n)
'''

# Given X = {0,1,2}
# How many X-String of length n that does not contain 20 as a substring. 
# Write a recursive function that returns the number of X-String of length n that does not contain 20 as a substring.

def recursive_x_string(n):
    if n == 0:
        return 1
    if n == 1:
        return 3
    return 2 * recursive_x_string(n-1) + recursive_x_string(n-2)

print(recursive_x_string(26)) # 9

