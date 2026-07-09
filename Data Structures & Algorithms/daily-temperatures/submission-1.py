class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        length = len(temperatures)
        stack = []
        i = 0
        count = 0
        output = [0 for t in temperatures]

        for t in range(0, length):
            curr = temperatures[t]
            while (stack and curr > temperatures[stack[-1]]):
                val = stack.pop()
                output[val] = t - val
            stack.append(t)
        return output