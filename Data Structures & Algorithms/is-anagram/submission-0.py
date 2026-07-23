from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        mapOne = defaultdict(int)
        mapTwo = defaultdict(int)

        for j in range(len(s)):
            mapOne[s[j]] += 1

        for k in range(len(t)):
            mapTwo[t[k]] += 1

        if mapOne == mapTwo:
            return True
        else:
            return False