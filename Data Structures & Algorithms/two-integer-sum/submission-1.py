class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        map = defaultdict(list)

        for i, num in enumerate(nums):
            j = target - num

            if j in map:
                return [map[j], i]

            map[num] = i

        return []

            


        

        