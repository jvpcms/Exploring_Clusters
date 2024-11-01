import numpy as np
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from utils.clusters import Cluster


class Point:
    def __init__(self, vector: List[float]):
        self.vector = np.array(vector)
        self.dimension = len(vector)

        self.color: str = "#555555"
        self.cluster_id: str | None = None
        self.changed_in_last_iteration: bool = False

    def distance(self, point: "Point") -> float:
        """Find the Euclidean distance between two points"""

        return float(np.linalg.norm(self.vector - point.vector))

    def cluster_with_closest_centroid(self, clusters: List["Cluster"]) -> "Cluster":
        """Find the cluster with the closest centroid to the point"""

        return min(clusters, key=lambda cluster: self.distance(cluster.centroid))

    def move_to_closest_cluster(self, clusters: List["Cluster"]):
        """Move the point to the cluster with the closest centroid"""

        closest_cluster = self.cluster_with_closest_centroid(clusters)

        # register if the point changed clusters from the last iteration
        if closest_cluster.id == self.cluster_id:
            self.changed_in_last_iteration = False
        else:
            self.changed_in_last_iteration = True

        closest_cluster.add_point(self)
