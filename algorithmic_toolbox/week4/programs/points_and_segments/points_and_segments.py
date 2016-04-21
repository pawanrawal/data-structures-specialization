# Uses python3
import sys
from operator import itemgetter

def fast_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    # forming an aggregate list
    aggregate = [[x, 'p'] for x in points]
    for e in range(len(starts)):
        if starts[e] <= ends[e]:
            aggregate = aggregate + [[starts[e], 'l'], [ends[e], 'r']]

    aggregate.sort(key = itemgetter(0))

    pointsdict = {points[i]: i for i in range(len(points))}

    opensegments = 0

    for elem in aggregate:
        if elem[1] == 'l':
            opensegments += 1
        elif elem[1] == 'r':
            opensegments -= 1
        elif elem[1] == 'p':
            cnt[pointsdict[elem[0]]] = opensegments

    return cnt

def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    #use fast_count_segments
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')
