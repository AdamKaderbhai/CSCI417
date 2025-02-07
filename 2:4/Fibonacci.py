def is_fibonacci(n):
    if n < 0:
        return False
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return b == n

test_case = [100000]

for i in test_case:
        print(is_fibonacci(i))
