def euclidean_algorithm(a, b):
    a, b = abs(a), abs(b)
    while b != 0:
        a, b = b, a % b
    return a