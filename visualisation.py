import matplotlib.pyplot as plt


def show_tracks_interactive(track_a: list, track_b: list, image_width: int, image_height: int, pause_time: int = 1):
    plt.ion()
    plt.xlim([0, 1920])
    plt.ylim([0, 1080])

    for i in range(max(len(track_a), len(track_b))):
        xs_a, ys_a = [p.x * image_width for p in track_a], [p.y * image_height for p in track_a]
        xs_b, ys_b = [p.x * image_width for p in track_b], [p.y * image_height for p in track_b]

        plt.plot(xs_a[0:min(i, len(track_a))], ys_a[0:min(i, len(track_a))])
        plt.plot(xs_b[0:min(i, len(track_b))], ys_b[0:min(i, len(track_b))])
        plt.draw()
        plt.pause(pause_time)

    plt.ioff()
    plt.show()
