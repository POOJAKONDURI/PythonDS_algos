def validparenthesis(exp):
    stack = []
    pairs = {'(':')','[':']','{':'}'}
    for char in exp:
        if char in pairs:
            stack.append(char)
        elif char in pairs.values():
            if not stack or pairs[stack.pop()] != char:
                return False
    return stack == []

def main():
    expr = '[()]'
    print(validparenthesis(expr))
if __name__ == "__main__":
    main()

