class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals=sorted(intervals)
        print(intervals)

        min_start=intervals[0][0]
        max_end=intervals[0][1]
        l=[]

        for start,end in intervals[1:]:
            if start<=max_end:
                max_end = max(max_end, end)
            else:
                l.append([min_start,max_end])
                min_start=start
                max_end=end
        l.append([min_start, max_end])
        return l
        