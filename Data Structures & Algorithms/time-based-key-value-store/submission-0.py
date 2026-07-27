class TimeMap:

    def __init__(self):
        self.timeMap = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeMap:
            self.timeMap[key] = []
        self.timeMap[key].append([value, timestamp])
        
    def get(self, key: str, timestamp: int) -> str:
        res = ""

        if key not in self.timeMap:
            return res

        arr = self.timeMap.get(key, [])
        
        lo = 0
        hi = len(arr)

        while (lo < hi):
            m = (lo + hi) // 2
            if arr[m][1] <= timestamp:
                lo = m + 1
            else:
                hi = m

        if lo > 0:
            res = arr[lo-1][0]
        
        return res
        
        


        
