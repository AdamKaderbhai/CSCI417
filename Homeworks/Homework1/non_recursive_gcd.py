def euclidean_alg(a,b):
    while a != 0 and b != 0:
        if a > b:
            a -= b
        else:
            b -= a
    return a if a != 0 else b
    
    
    
def non_recursive_gcd(alist):
    if len(alist) == 0:
        return None
    result = alist[0]
    for num in alist[1:]:
        result = euclidean_alg(result, num)
    return result

alist = input("Enter a list of numbers separated by spaces: ")
alist = [int(x) for x in alist.split()]

result = non_recursive_gcd(alist)
print("The GCD of alist is: ", result)


    
