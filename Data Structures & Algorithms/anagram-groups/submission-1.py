class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        map = defaultdict(list)

        for i in (strs): # Runs over number of words
            count = [0] * 26

            for c in i: # How many times each character appears in a word
                count[ord(c) - ord('a')] += 1

            map[tuple(count)].append(i) # Cant use list as a key in python

        return list(map.values())        