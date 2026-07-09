class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        output = 0

        if (len(tokens) <= 1):
            return int(tokens[0])

        for i in range(len(tokens)):
            if (tokens[i] in "+-*/" and (len(stack) > 1)):

                output = 0

                val1 = int(stack.pop())
                val2 = int(stack.pop())

                print(f"Val 1: {val1}")
                print(f"Val 2: {val2}")

                if (tokens[i] == "+"):
                   output += (val1 + val2)
                if (tokens[i] == "-"):
                    output += (val2 - val1)
                if (tokens[i] == "*"):
                    output += (val1 * val2) 
                if (tokens[i] == "/"):
                    output += int(val2 / val1) 
                
                print(f"Output: {output}")
                stack.append(output)

            else:
                stack.append(tokens[i])
                print(tokens[i])
            
        return output
