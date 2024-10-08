class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop() if self.items else None
    
    def is_empty(self):
        return len(self.items) == 0

def reverse_string(s):
    stack = Stack()
    
    # Push all characters to stack
    for char in s:
        stack.push(char)
    
    # Pop all characters from stack to reverse
    reversed_str = ""
    while not stack.is_empty():
        reversed_str += stack.pop()
    
    return reversed_str

# Test
string = "hello"
print("Original String:", string)
print("Reversed String:", reverse_string(string))
