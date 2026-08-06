class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda x:x[0])
        print(intervals)

        prev = intervals[0]
        result = []

        if len(intervals) == 1:
            result.append(intervals[0])
        else:
            for i in range(1, len(intervals)):

                curr = intervals[i]

                if curr[0] <= prev[1]:
                    prev = [min(prev[0], curr[0]), max(curr[1], prev[1])]
                else:
                    result.append(prev)
                    prev = curr

            result.append(prev)

        return result   