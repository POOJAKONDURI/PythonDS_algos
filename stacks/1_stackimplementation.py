'''

    @Author:pooja
    @Date:23-09-2024
    @last modified by:pooja
    @last modified time:23-09-2024
    @title:stack implementation 

'''

class Stack:
    def __init__(self):
        self.stack = []

    # Push an element to the stack
    def push(self, element):
        self.stack.append(element)

    # Pop an element from the stack
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return "Stack is empty"

    # Peek at the top element without removing it
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return "Stack is empty"

    # Check if the stack is empty
    def is_empty(self):
        return len(self.stack) == 0

    # Display the stack elements
    def display(self):
        return self.stack
def main():
    s = Stack()
    s.push(10)
    s.push(20)
    s.push(30)

    print("Stack:", s.display())  # Output: Stack: [10, 20, 30]

    print("Top Element:", s.peek())  # Output: Top Element: 30

    s.pop()  # Removes 30
    print("After pop:", s.display())  # Output: After pop: [10, 20]

if __name__ =='__main__':
    main()