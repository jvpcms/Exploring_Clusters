import sys

sys.path.append("..")

from typing import List
from utils.clusters import Cluster
from utils.points import Point
from utils.benchmark import load_benchmark
from utils.plot import (
    display_start,
    display_end,
    display_clear,
    display_points,
    display_clusters_centroids,
    display_refresh,
)


def k_means(points: List[Point], k: int) -> List[Cluster]:
    clusters = [Cluster(points) for _ in range(k)]

    display_points(points)
    display_clusters_centroids(clusters)
    display_refresh()

    # K-means algorithm
    points_changed_clusters = True
    while points_changed_clusters:
        display_clear()

        # Points move to cluster with closest centroid
        points_changed_clusters = False
        for p in benchmark:
            p.move_to_closest_cluster(clusters)

            if p.changed_in_last_iteration:
                points_changed_clusters = True

        # Update cluster centroids
        for c in clusters:
            c.update_centroid()
            c.reset_points()

        display_points(benchmark)
        display_clusters_centroids(clusters)
        display_refresh()

    return clusters


if __name__ == "__main__":
    # Setup
    BENCHMARK_FILE = "s1"
    NUMBER_OF_CLUSTERS = 15

    display_start()

    benchmark = load_benchmark(BENCHMARK_FILE)

    k_means(benchmark, NUMBER_OF_CLUSTERS)
    # clusters = [Cluster(benchmark) for _ in range(NUMBER_OF_CLUSTERS)]
    #
    # display_points(benchmark)
    # display_clusters_centroids(clusters)
    # display_refresh()
    #
    # # K-means algorithm
    # points_changed_clusters = True
    # while points_changed_clusters:
    #     display_clear()
    #
    #     # Points move to cluster with closest centroid
    #     points_changed_clusters = False
    #     for p in benchmark:
    #         p.move_to_closest_cluster(clusters)
    #
    #         if p.changed_in_last_iteration:
    #             points_changed_clusters = True
    #
    #     # Update cluster centroids
    #     for c in clusters:
    #         c.update_centroid()
    #         c.reset_points()
    #
    #     display_points(benchmark)
    #     display_clusters_centroids(clusters)
    #     display_refresh()

    display_end()
