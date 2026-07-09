class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        map = defaultdict(list)
        count = 1
        output = []

        if (len(nums) < 1):
            return 0

        for n in nums:
            map[n].append(n)
        
        for i in map:
            if (i-1) not in map:
                count = 1
                while( (i+1) in map):
                    count += 1
                    i += 1
            output.append(count)

        return max(output)
            
        