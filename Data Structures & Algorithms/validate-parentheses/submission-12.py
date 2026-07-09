class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        for i in range(0, len(s)):
            if (s[i] in "([{"):
                stack.append(s[i])

            if (s[i] in ")]}"):
                if (len(stack) == 0):
                    return False
                if (len(stack) > 0):
                    if (stack[-1] == '(' and s[i] == ')'):
                        stack.pop()
                    elif (stack[-1] == '[' and s[i] == ']'):
                        stack.pop() 
                    elif (stack[-1] == '{' and s[i] == '}'):
                        stack.pop()
                    else:
                        return False
        
        if (len(stack) == 0):
            return True
        else:
            return False



        