class Solution:
    def trap(self, height: List[int]) -> int:

        length = len(height)
        leftMax = 0
        rightMax = 0
        
        maxLeft = [0] * length
        maxRight = [0] * length 

        area = 0
        i = 0

        for i in range(len(height)):
            leftMax = max(height[i], leftMax)
            maxLeft[i] = leftMax

        for i in range(len(height)):
            rightMax = max(height[length-1-i], rightMax)
            maxRight[length-1-i] = rightMax

        for i in range(len(height)):
            val = min(maxLeft[i], maxRight[i])
            if (val-height[i] > 0):
                area += (val-height[i])

        return area

    #Runtime: O(n) + O(n) + O(n) = O(3n) = O(n)
    #Space Complexity: 2 arrays of size length are created -> O(2n) = O(n)

            
        