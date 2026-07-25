from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        res = 0
        hashMap = defaultdict(int)
        for i in range(len(nums)):
            hashMap[nums[i]] += 1

            if (hashMap[nums[i]] > (len(nums)/2)):
                res = nums[i]
        return res

        