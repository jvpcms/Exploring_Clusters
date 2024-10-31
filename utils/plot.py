from typing import List
import matplotlib.pyplot as plt
from utils.points import Point
from utils.clusters import Cluster

FRAME_INTERVAL = 0.1


def display_start():
    plt.ion()
    plt.show()


def display_clear():
    plt.clf()


def display_points(points: List[Point]):
    plt.scatter(
        [point.vector[0] for point in points],
        [point.vector[1] for point in points],
        c=[point.color for point in points],
    )


def display_clusters_centroids(clusters: List[Cluster]):
    plt.scatter(
        [cluster.centroid.vector[0] for cluster in clusters],
        [cluster.centroid.vector[1] for cluster in clusters],
        color="black",
        marker="x",
    )


def display_refresh():
    plt.draw()
    plt.pause(FRAME_INTERVAL)


def display_end():
    print("Ending display")
    plt.ioff()
    plt.show()
