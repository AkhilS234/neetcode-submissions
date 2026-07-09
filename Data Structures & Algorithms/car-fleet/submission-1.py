class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        arr = []

        for p in range(len(position)):
            curr = [(position[p]), speed[p]]
            arr.append(curr)
        arr.sort(key=lambda x:x[0], reverse=True)
    
        stack = [-1]
        for i in range(len(arr)):
            (j, k) = arr[i]
            num = ((target-j)/k)
            if num <= stack[-1]:
                continue
            else:
                stack.append(num)
        
        count = 0
        for s in stack:
            if s > 0:
                count += 1
        
        return count
                