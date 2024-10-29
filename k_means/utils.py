from typing import List
import random
from uuid import uuid4


class Point:
    def __init__(self, x: float, y: float):
        self.x: float = x
        self.y: float = y
        self.color: str = "#000000"
        self.last_cluster_id: str | None = None
        self.changed_in_last_iteration: bool = False

    def distance(self, point: "Point"):
        dx = self.x - point.x
        dy = self.y - point.y

        return (dx**2 + dy**2) ** (1 / 2)

    def cluster_with_closest_centroid(self, clusters: List["Cluster"]):
        return min(clusters, key=lambda cluster: self.distance(cluster.centroid))

    def move_to_closest_cluster(self, clusters: List["Cluster"]):
        closest_cluster = self.cluster_with_closest_centroid(clusters)

        if closest_cluster.id == self.last_cluster_id:
            self.changed_in_last_iteration = False
        else:
            self.changed_in_last_iteration = True

        # Update the cluster assignment
        closest_cluster.points.append(self)
        self.color = closest_cluster.color
        self.last_cluster_id = closest_cluster.id

    @staticmethod
    def load_benchmark(file: str) -> List["Point"]:
        points = []

        with open(f"benchmark/{file}") as f:
            for line in f:
                position = line.strip().split(" ")
                position = list(filter(lambda x: x != "", position))

                x = int(position[0])
                y = int(position[1])

                points.append(Point(x, y))

        return points


class Cluster:
    def __init__(self, all_points: List[Point]):
        self.id: str = str(uuid4())
        self.points: List[Point] = []
        self.centroid: Point = random.choice(all_points)
        self.color = f"#{random.randint(0, 0xFFFFFF):06x}"

    def reset_points(self):
        self.points = []

    def update_centroid(self):
        if len(self.points) == 0:
            return

        x = sum([point.x for point in self.points]) / len(self.points)
        y = sum([point.y for point in self.points]) / len(self.points)

        self.centroid = Point(x, y)
