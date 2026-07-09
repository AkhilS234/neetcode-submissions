class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        map = defaultdict(list)
        output = []

        if (len(nums) < 1):
            return output

        for i in range(len(nums)):
            j = i+1 
            while (i<j and j < len(nums)):
                sum = nums[i]+nums[j]
                #print(sum)
                map[sum] = [i,j]
                j += 1
            
        if target in map:
            return map[target]


        

        