import sys

sys.path.append("..")

from utils.clusters import Cluster
from utils.benchmark import load_benchmark
from utils.plot import (
    display_start,
    display_end,
    display_clear,
    display_points,
    display_clusters_centroids,
    display_refresh,
)


# Setup
BENCHMARK_FILE = "s1"
NUMBER_OF_CLUSTERS = 15

benchmark = load_benchmark(BENCHMARK_FILE)
clusters = [Cluster(benchmark) for _ in range(NUMBER_OF_CLUSTERS)]

display_start()

display_points(benchmark)
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


display_end()
