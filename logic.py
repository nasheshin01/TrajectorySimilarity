import pandas as pd

import constants
import track_math

from track_structures import Point, LineSegment
from typing import List, Dict


def read_tracks(path: str, image_width: int, image_height: int) -> Dict[int, List[Point]]:
    df = pd.read_csv(path, sep=';')
    df['time'] = pd.to_datetime(df['time'])
    df_grouped_by_track = df.groupby('track')

    tracks = {}
    for track_group in df_grouped_by_track:
        track_group_ordered_by_time = track_group[1].sort_values('time')
        xs = track_group_ordered_by_time['x'].values.tolist()
        ys = track_group_ordered_by_time['y'].values.tolist()

        tracks[track_group[0]] = []
        for x, y in zip(xs, ys):
            tracks[track_group[0]].append(Point(x / image_width, y / image_height))

    return tracks


def remove_linear_points(track: List[Point]) -> List[Point]:
    track_new = [track[0]]
    for i in range(len(track) - 2):
        point_a = track[i]
        point_b = track[i + 2]
        common_point = track[i + 1]
        angle = track_math.angle(common_point, point_a, point_b)

        if 180 - angle > constants.ANGLE_THRESHOLD:
            track_new.append(common_point)

    track_new.append(track[-1])

    return track_new


# Функция определяет совпадения траекторий по отрезкам между точками
def get_track_similarity(track_a: List[Point], track_b: List[Point]) -> float:
    line_segments_a = LineSegment.line_segments_from_track(track_a)
    line_segments_b = LineSegment.line_segments_from_track(track_b)

    not_similar_count = len(line_segments_a) + len(line_segments_b)
    for line_segment_a in line_segments_a:

        closest_segment = (None, None)
        for line_segment_b in line_segments_b:
            is_close, distance = line_segment_a.is_close(line_segment_b)
            if not is_close:
                continue

            if closest_segment[0] is None:
                closest_segment = line_segment_b, distance
            else:
                if distance < closest_segment[1]:
                    closest_segment = line_segment_b, distance

        if closest_segment[0] is not None:
            line_segments_b.remove(closest_segment[0])
            not_similar_count -= 2

    return 1 - not_similar_count / (len(line_segments_a) + len(line_segments_b))