class Solution:
    def maxArea(self, heights: List[int]) -> int:

        ptr1 = 0
        ptr2 = len(heights)-1

        minHeight = min(heights[ptr1], heights[ptr2])
        width = ptr2-ptr1
        area = minHeight * width

        tempArea = 0
        p1 = ptr1
        p2 = ptr2
        w = width

        while (p1 < p2):
            
            if (min(heights[p1], heights[p2]) == heights[p1]):
                p1 += 1
                w -= 1

            elif (min(heights[p1], heights[p2]) == heights[p2]):
                p2 -= 1
                w -= 1

            tempArea = min(heights[p1], heights[p2]) * w

            if (tempArea > area):
                area = tempArea
                ptr1 = p1
                ptr2 = p2
   # /*        else:
     #           if (p1 != ptr1):
     #               p1 = ptr1
     #           if (p2 != ptr2):
     #               p2 = ptr2
            

            print(f"ptr 1: {heights[ptr1]}, ptr 2:{heights[ptr2]}")

        return area