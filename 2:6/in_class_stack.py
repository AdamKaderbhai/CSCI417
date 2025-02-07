class Stack():
    
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[len(self.items)-1] 
    
    def size(self):
        return len(self.items)
    


'''def convert_to_decimal(s):
    #s = 1101 = 1 * 2 ** 3 + 1 * 2 ** 2 + 0 * 2 ** 1 + 1 * 2 ** 0 
    decimal = 0
    for i in range(len(s)):
        decimal += int(s[i]) * (2 ** (len(s) - 1 - i))
    return decimal
print(convert_to_decimal('1101'))'''

'''
def convert_to_binary(n):
    stack = Stack()
    while n > 0:
        remainder = n % 2
        stack.push(remainder)
        n = n // 2
    
    binary = ""
    while not stack.isEmpty():
        binary += str(stack.pop())
    
    return binary

# testcases
Test_Cases = range(1, 1000)
for i in Test_Cases:
    print(f"Binary of {i} is {convert_to_binary(i)}")

'''
def balanced_parentheses(s):
    stack = Stack()
    for i in s:
        if i == '(':
            stack.push(i)
        elif i == ')':
            if stack.isEmpty():
                return False
            stack.pop()
    return stack.isEmpty()

# testcases

print(balanced_parentheses('()()'))
