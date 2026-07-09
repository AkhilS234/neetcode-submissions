class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        length = len(temperatures)
        stack = []
        i = 0
        count = 0
        output = [0 for t in temperatures]

        while (i < length):
            stack.append(temperatures[i])
            count = 0
            for t in range(i+1, length):
                if temperatures[t] > stack[-1]:
                    count += 1
                    output[i] = count
                    stack.clear()
                    break
                else:
                    count += 1
            i += 1
        return output