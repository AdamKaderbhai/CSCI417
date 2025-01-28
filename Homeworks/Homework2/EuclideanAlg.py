"""
def leastabsremainder(a, b):
    q = b // a
    r = b - (a*q)

    if abs(r) <= a / 2:
        return r
    else:
        return r - a
    
def greatestcommondivisor(a, b):
    while b != 0:
        a, b = a, leastabsremainder(a, b)
    return abs(a)

test_cases = [
    (7,20)
]
for a, b in test_cases:
    result = greatestcommondivisor(a, b)
    print(f"greatestcommondivisor({a}, {b}) = {result}")

   
def numeric_values(a_list):
    for i in a_list:
        if type(i) != int:
            return False
        else:
            return True

a_list = ["1", "apple", 1, 1.2, -4]
"""

class ComplexNumber:
    def __init__()
    
  

        


  
