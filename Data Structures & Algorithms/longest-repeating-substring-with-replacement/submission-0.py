class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        length = len(s)
        l = 0
        result = 0
        seen = defaultdict(int)

        for r in range(len(s)):
            seen[s[r]] = 1 + seen.get(s[r], 0)  

            while ((r-l + 1) - max(seen.values())) > k :
                seen[s[l]] -= 1
                l += 1

            result = max(result, r-l+1)
        
        return result

