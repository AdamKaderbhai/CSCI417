def divisor_set(a):
    # return the divisor set of a
    a = abs(a)
    div_set = set()
    for d in range(1, a+1):
        if a %d == 0:
            div_set.add(d)
    return div_set
def divisor_set_new(a):
    n = abs(a)
    div_set = set()
    i = 1
    while i<n+1:
        if n % i == 0:
            div_set.add(i)
        i +=1
    return div_set

def first_gcd_alg(a,b):
    div_a = divisor_set(a)
    div_b = divisor_set(b)
    common_div = div_a.intersection(div_b)
    return max(common_div)
def second_gcd_alg(a,b):
    a, b = min(abs(a), abs(b)), max(abs(a), abs(b))
    div_a = divisor_set(a)
    current_max = 1
    for n in div_a:
        if (b%n ==0) and n>current_max:
            current_max = n
    return current_max
def third_gcd_alg(a,b):
    a, b = min(abs(a), abs(b)), max(abs(a), abs(b))
    i = a
    while i>0:
        if (a % i ==0) and (b % i ==0):
            return i
        i -=1
def recursive_factorial(n):
    if n == 1:
        return 1
    else:
        return n * recursive_factorial(n-1)
def non_rc_factorial(n):
    result = 1
    for i in range(1,n+1):
        result *=i
    return result









a = 10
div_set = divisor_set(a)
print(div_set)
a = -5
div_set = divisor_set(a)
print(div_set)
a = 77
div_set = divisor_set_new(a)
print(div_set)

a = 26
b = 4
print(first_gcd_alg(a,b))
print(second_gcd_alg(a,b))
print(third_gcd_alg(a,b))
print(recursive_factorial(4))
print(non_rc_factorial(4))



