# (Q1) Valid Parentheses

# TC: O(n) SC: O(n) 
def validParantheses(str):
    stack = []
    for s in str:
        if (s == '(' or s == '{' or s == '['):
            stack.append(s)
        elif s == ')' or s == '}' or s == ']':
            if len(stack) == 0: return False
            top = stack.pop()
            if (s == '(' and top != ')') or \
                (s == '{' and top != '}') or  \
                (s == '[' and top != ']'):
                return False
    return len(stack) == 0            

# print(validParantheses("()[]{}"))


# (Q2) 