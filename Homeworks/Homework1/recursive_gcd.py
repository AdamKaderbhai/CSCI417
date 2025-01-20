alist = input("Enter a list of numbers separated by spaces: ")
alist = [int(x) for x in alist.split()]

def euclidean_alg(a,b):
    while a != 0 and b != 0:
        if a > b:
            a -= b
        else:
            b -= a
    return a if a != 0 else b
    
    
def recursive_gcd(alist):
    if len(alist) == 0:
        return None
    elif len(alist) == 1:
        return alist[0]
    else:
        return euclidean_alg(alist[0], recursive_gcd(alist[1:]))
    
result = recursive_gcd(alist)

print("The GCD of alist is: ", result)

    
        
    

    


