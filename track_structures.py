import constants

from typing import List


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other_point):
        if not isinstance(other_point, Point):
            return False

        return ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5


class LineSegment:

    def __init__(self, start_point: Point, end_point: Point):
        self.start_point = start_point
        self.end_point = end_point
        self.distance_threshold = constants.POINT_DISTANCE_THRESHOLD

    def is_close(self, other_line_segment):
        if not isinstance(other_line_segment, LineSegment):
            return False, -1

        start_points_distance = self.start_point.distance(other_line_segment.start_point)
        end_points_distance = self.end_point.distance(other_line_segment.end_point)

        is_close = start_points_distance < self.distance_threshold and end_points_distance < self.distance_threshold
        distance_sum = start_points_distance + end_points_distance

        return is_close, distance_sum

    @staticmethod
    def line_segments_from_track(track: List[Point]):
        line_segments = []
        for i in range(len(track) - 1):
            line_segments.append(LineSegment(track[i], track[i + 1]))

        return line_segments

