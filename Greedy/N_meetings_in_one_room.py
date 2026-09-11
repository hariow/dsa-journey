## N meeting in one room

class Meeting:

    def __init__(self, start, end, position):
        self.start = start
        self.end = end
        self.position = position

def solve():
    start = [0, 3, 1, 6, 7, 11]
    end = [6, 5, 2, 8, 10, 15]

    n = len(start)
    # meet=[]
    meet = [Meeting(start[i], end[i], i + 1) for i in range(n)]

    meet.sort(key=lambda x: (x.end, x.start))

    result = [meet[0].position]
    count = 1

    last_time = meet[0].end

    for i in range(1, n):
        if meet[i].start > last_time:
            count += 1
            result.append(meet[i].position)
            last_time = meet[i].end

    return count

print(solve())