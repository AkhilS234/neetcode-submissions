class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        nums.sort()
        result = []

        def dfs(i, cur, total):
            if total == target:
                result.append(cur.copy())
                return 

            if (i >= len(nums)) or (total > target):
                return 

            #Every recursive call has two chices

            #Choice 1 - Take the current number

            cur.append(nums[i])
            dfs(i, cur, total + nums[i])

            #Choice 2 - Skip the current number

            cur.pop()
            dfs(i+1, cur, total)

        dfs(0, [], 0)
        return result

        

        