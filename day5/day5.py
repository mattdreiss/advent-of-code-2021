class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if not isinstance(other, Point):
            return False
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash(self.x) + hash(self.y)

    def __str__(self):
        return f'({self.x},{self.y})'


class Segment:
    def __init__(self, point0, point1):
        self.p0 = point0
        self.p1 = point1
        self.is_straight = point0.x == point1.x or point0.y == point1.y
        self.points = None

    def build_segment(self):
        result = [self.p0]
        x_delta = -1 if self.p1.x < self.p0.x else 1
        y_delta = -1 if self.p1.y < self.p0.y else 1

        next_point = self.p0
        while next_point != self.p1:
            next_x = next_point.x + x_delta if next_point.x != self.p1.x else next_point.x
            next_y = next_point.y + y_delta if next_point.y != self.p1.y else next_point.y
            next_point = Point(next_x, next_y)
            result.append(next_point)
        self.points = result
        return result


def process_line(line):
    points = line.strip().split(' -> ')
    p0 = points[0].split(',')
    p1 = points[1].split(',')
    return Segment(Point(int(p0[0]), int(p0[1])), Point(int(p1[0]), int(p1[1])))


def read_input():
    with open('input.txt', 'r') as input_file:
        lines = input_file.readlines()
        return [process_line(line) for line in lines]


def part1():
    segments = read_input()
    straight_segments = list(filter(lambda s: s.is_straight, segments))
    vent_locations = {}
    dangerous_location_count = 0
    for segment in straight_segments:
        for point in segment.build_segment():
            if point in vent_locations:
                vent_locations[point] += 1
            else:
                vent_locations[point] = 1
    for vent_location in vent_locations.items():
        if vent_location[1] > 1:
            dangerous_location_count += 1
    print(dangerous_location_count)


def part2():
    segments = read_input()
    vent_locations = {}
    dangerous_location_count = 0
    for segment in segments:
        for point in segment.build_segment():
            if point in vent_locations:
                vent_locations[point] += 1
            else:
                vent_locations[point] = 1
    for vent_location in vent_locations.items():
        if vent_location[1] > 1:
            dangerous_location_count += 1
    print(dangerous_location_count)


part1()
part2()
