import logic
import constants
import sys


def main():
    tracks_path = sys.argv[1]
    track_a_index = int(sys.argv[2])
    track_b_index = int(sys.argv[3])

    tracks = logic.read_tracks(tracks_path, constants.IMAGE_WIDTH, constants.IMAGE_HEIGHT)
    track_a, track_b = tracks[track_a_index], tracks[track_b_index]

    # Необходимо, чтобы убрать точки, которые находятся на относительно прямых участках траектории
    track_a_cleared = logic.remove_linear_points(track_a)
    track_b_cleared = logic.remove_linear_points(track_b)

    similarity = logic.get_track_similarity(track_a_cleared, track_b_cleared)
    if similarity == 1:
        print("Total similarity")
    elif 0.7 < similarity < 1:
        print("Partial similarity")
    else:
        print("No similarity")


if __name__ == "__main__":
    main()
