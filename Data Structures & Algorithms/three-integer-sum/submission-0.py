class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        length = len(nums)
        i = 0
        output = []
        while (i < length):
            l = i + 1
            r = length - 1

            while ((l < r)):
                sum = nums[i] + nums[l] + nums[r]

                if (sum == 0):
                    ans = [nums[i], nums[l], nums[r]]
                    if ans not in output:
                        output.append(ans)
                    l += 1
                    r -= 1
                elif (sum < 0):
                    l += 1
                else:
                    r -= 1
                
            i += 1
        return output

