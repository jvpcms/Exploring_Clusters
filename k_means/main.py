from utils import Point, Cluster
import matplotlib.pyplot as plt


BENCHMARK_FILE = "s1.txt"
NUMBER_OF_CLUSTERS = 15
FRAME_INTERVAL = 0.1


def update_display(points, clusters):
    plt.clf()  # Clear the current figure

    # Plot points
    plt.scatter(
        [point.x for point in points],
        [point.y for point in points],
        c=[point.color for point in points],
    )

    # Plot cluster centroids
    plt.scatter(
        [cluster.centroid.x for cluster in clusters],
        [cluster.centroid.y for cluster in clusters],
        color="black",
        marker="x",
    )

    # Refresh the plot
    plt.draw()
    plt.pause(FRAME_INTERVAL)


benchmark = Point.load_benchmark(BENCHMARK_FILE)
clusters = [Cluster(benchmark) for _ in range(NUMBER_OF_CLUSTERS)]

points_changed_clusters = True
while points_changed_clusters:
    update_display(benchmark, clusters)

    # Points move to cluster with closest centroid
    points_changed_clusters = False
    for p in benchmark:
        p.move_to_closest_cluster(clusters)

        if p.changed_in_last_iteration:
            points_changed_clusters = True

    update_display(benchmark, clusters)

    # Update cluster centroids
    for c in clusters:
        c.update_centroid()


print("Clustering stable")
plt.ioff()
plt.show()
