# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    last_added_point = None
    current_index = 0
    # sorting segments by their end value
    segments = sorted(segments, key=lambda segment: segment.end)
    n = len(segments)

    while current_index < n:
        s = segments[current_index]
        # storing last added point, so that it can be used later
        last_added_point = s.end
        # adding the point to points list.
        points.append(s.end)
        current_index += 1
        # while the other segments contain this point and the index < n , we keep on increasing current index.
        while current_index < n and segments[current_index].start <= last_added_point <= segments[current_index].end:
            current_index +=1

    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
