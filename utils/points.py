from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from utils.clusters import Cluster


class Point:
    def __init__(self, x: float, y: float):
        self.x: float = x
        self.y: float = y
        self.color: str = "#555555"
        self.last_cluster_id: str | None = None
        self.changed_in_last_iteration: bool = False

    def distance(self, point: "Point"):
        """Find the Euclidean distance between two points"""

        dx = self.x - point.x
        dy = self.y - point.y

        return (dx**2 + dy**2) ** (1 / 2)

    def cluster_with_closest_centroid(self, clusters: List["Cluster"]):
        """Find the cluster with the closest centroid to the point"""

        return min(clusters, key=lambda cluster: self.distance(cluster.centroid))

    def move_to_closest_cluster(self, clusters: List["Cluster"]):
        """Move the point to the cluster with the closest centroid"""

        closest_cluster = self.cluster_with_closest_centroid(clusters)

        if closest_cluster.id == self.last_cluster_id:
            self.changed_in_last_iteration = False
        else:
            self.changed_in_last_iteration = True

        closest_cluster.points.append(self)
        self.color = closest_cluster.color
        self.last_cluster_id = closest_cluster.id
