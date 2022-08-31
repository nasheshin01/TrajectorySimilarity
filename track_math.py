import math

from track_structures import Point


def angle(com_point: Point, point_a: Point, point_b: Point):
    x1, y1 = (point_a.x - com_point.x, point_a.y - com_point.y)
    x2, y2 = (point_b.x - com_point.x, point_b.y - com_point.y)

    inner_product = x1 * x2 + y1 * y2
    len1 = math.hypot(x1, y1)
    len2 = math.hypot(x2, y2)
    return math.degrees(math.acos(inner_product / (len1 * len2)))
