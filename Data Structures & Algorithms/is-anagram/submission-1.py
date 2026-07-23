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

# Space Complexity is determined by how large the maps can grow as the input grows
# Since the number of input characters is restricted to 26 lowercase letters, O(26) = O(1)
