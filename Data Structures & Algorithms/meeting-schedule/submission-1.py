"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x:x.end)
        if not intervals:
            return True
        curE = intervals[0].end
        
        for i in range(1, len(intervals)):
            if intervals[i].start < curE:
                return False
            curE = intervals[i].end

        
        return True