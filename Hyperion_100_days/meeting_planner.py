intervals = [[0,30],[5,10],[15,20]]
intervals2 = [[0,5],[5,10],[10,20]]

def can_attend(intervals):
    end_time = intervals[0][1]
    for time in intervals[1:]:
        if end_time <= time[1] and end_time <= time[0]:
            end_time = time[1]
        else: return False
    return True


print(can_attend(intervals))
print(can_attend(intervals2))