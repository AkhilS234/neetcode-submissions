class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        i = 0
        j = 0
        window = len(s1)
        l = 0
        r = 0 
        seen = defaultdict(int)
        word = defaultdict(int)
        
        for i in range(len(s1)):
            word[s1[i]] += 1

        if (len(s1) > len(s2)):
            return False

        for i in range(window):
            seen[s2[r]] += 1
            r += 1
        
        while (r < len(s2)):
            if (seen == word):
                return True
            else:
                seen[s2[r]] += 1
                seen[s2[l]] -= 1
                if (seen[s2[l]] == 0):
                    del seen[s2[l]]
                l += 1
                r += 1
        return seen == word